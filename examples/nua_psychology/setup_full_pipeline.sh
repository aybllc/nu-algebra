#!/bin/bash
# ============================================================
# Setup full N/U Psychology pipeline on RHEL
# 1. Exports psymetadata .rda -> CSV into datasets/
# 2. Creates analysis scripts
# ============================================================

BASE_DIR="/root/Documents/nu_math/v4/gradschool"
PSYMETADATA_DIR="/root/Documents/nu_math/v4/gradschool/psymetadata-main"

# Ensure dirs exist
mkdir -p $BASE_DIR/analysis
mkdir -p $BASE_DIR/datasets
mkdir -p $BASE_DIR/results
mkdir -p $BASE_DIR/paper

# Step 1: Create R script to export datasets
echo "Creating export_psymetadata.R..."
cat > $BASE_DIR/analysis/export_psymetadata.R <<'EOF'
# Export selected psymetadata datasets to CSV

datasets <- c("barroso2021", "noble2019", "sala2019", "maccann2020",
              "manylabs2018", "manybabies2020", "facial_feedback",
              "nuijten2020", "future_thinking_depression", "juvenile_recidivism")

outdir <- file.path(Sys.getenv("BASE_DIR", "/root/Documents/nu_math/v4/gradschool"), "datasets")
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)

for (d in datasets) {
  message("Exporting: ", d)
  data(list = d, package = "psymetadata")   # load dataset
  df <- get(d)

  df_out <- data.frame(
    StudyID = 1:nrow(df),
    EffectSize = df$yi,
    SE = sqrt(df$vi),
    CI_low = df$yi - 1.96*sqrt(df$vi),
    CI_high = df$yi + 1.96*sqrt(df$vi)
  )

  write.csv(df_out, file.path(outdir, paste0(d, "_meta.csv")), row.names = FALSE)
}
EOF

# Step 2: Create Python N/U script
echo "Creating analysis_nu.py..."
cat > $BASE_DIR/analysis/analysis_nu.py <<'EOF'
import pandas as pd
import json
import os

def run_nu_meta(csv_path):
    """
    Conservative N/U algebra bounds for a meta-analysis dataset.
    """
    df = pd.read_csv(csv_path)
    df["u_nu"] = df["SE"].abs() * 1.96
    df["lower"] = df["EffectSize"] - df["u_nu"]
    df["upper"] = df["EffectSize"] + df["u_nu"]

    outpath = os.path.join("results", os.path.basename(csv_path).replace(".csv","_nu.json"))
    os.makedirs("results", exist_ok=True)
    df.to_json(outpath, orient="records", indent=2)

    return {
        "nu_bounds": [float(df["lower"].min()), float(df["upper"].max())],
        "rows": int(len(df))
    }
EOF

# Step 3: Create R master analysis script
echo "Creating run_all_meta.R..."
cat > $BASE_DIR/analysis/run_all_meta.R <<'EOF'
library(metafor)
library(brms)
library(tidyverse)
library(reticulate)

dataset_dir <- "datasets"
results_dir <- "results"
dir.create(results_dir, showWarnings = FALSE)

files <- list.files(dataset_dir, pattern = "_meta.csv$", full.names = TRUE)

nu <- import_from_path("analysis_nu", path = "analysis")

all_results <- list()

for (f in files) {
  cat("Processing:", f, "\n")
  df <- read.csv(f)
  dataset_name <- tools::file_path_sans_ext(basename(f))

  # Frequentist
  freq_summary <- NULL
  try({
    res <- rma(yi = EffectSize, sei = SE, data = df, method = "REML")
    freq_summary <- summary(res)
    png(file.path(results_dir, paste0(dataset_name, "_forest.png")), width=800, height=600)
    forest(res, main = paste("Forest Plot -", dataset_name))
    dev.off()
  })

  # Bayesian
  bayes_summary <- NULL
  try({
    bmodel <- brm(EffectSize | se(SE) ~ 1 + (1|StudyID),
                  data = df,
                  prior = c(prior(normal(0,1), class=Intercept),
                            prior(cauchy(0,1), class=sd)),
                  iter = 2000, chains = 2, seed = 123,
                  refresh = 0)
    bayes_summary <- summary(bmodel)
  })

  # N/U (Python)
  nu_result <- NULL
  try({
    nu_result <- nu$run_nu_meta(f)
  })

  all_results[[dataset_name]] <- list(
    frequentist = freq_summary,
    bayesian = bayes_summary,
    nu = nu_result
  )
}

saveRDS(all_results, file.path(results_dir, "all_meta_results.rds"))
writeLines(capture.output(str(all_results)), con = file.path(results_dir, "all_meta_results.txt"))
EOF

echo "Setup complete!"
echo "Next steps:"
echo "1. In R, run: source('$BASE_DIR/analysis/export_psymetadata.R')"
echo "   → This will export 10 meta-analysis datasets into $BASE_DIR/datasets/"
echo "2. Then run: Rscript $BASE_DIR/analysis/run_all_meta.R"
echo "   → This will process all datasets with Frequentist, Bayesian, and N/U pipelines."
