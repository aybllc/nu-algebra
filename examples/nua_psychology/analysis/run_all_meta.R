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
