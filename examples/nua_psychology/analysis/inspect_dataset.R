# ==========================================================
# Inspect a psymetadata dataset
# Usage: Rscript analysis/inspect_dataset.R dataset_name
# Example: Rscript analysis/inspect_dataset.R manylabs2018
# ==========================================================

args <- commandArgs(trailingOnly = TRUE)

if (length(args) == 0) {
  stop("Please provide a dataset name, e.g. manylabs2018")
}

dataset <- args[1]

library(psymetadata)

cat("Loading dataset:", dataset, "\n")
data(list = dataset, package = "psymetadata")
df <- get(dataset)

cat("\n--- Structure ---\n")
str(df)

cat("\n--- First 6 rows ---\n")
print(head(df))

cat("\n--- Column names ---\n")
print(names(df))
