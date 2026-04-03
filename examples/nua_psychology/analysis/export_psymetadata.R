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
