# Swensson et al. Figure 1 digitization report

## Scope

This file documents a digitized reconstruction of Figure 1 from Swensson et al. (2024). Values are approximate extractions from the published figure, not author-provided raw data. The response axis is discrete 0-5, and extracted values were snapped to the nearest integer.

## Calibration

| Participant | x0 px/session0 | x px/session | y0 px/response0 | y px/response | five-target change session approx |
|---|---:|---:|---:|---:|---:|
| Alex | 113.5 | 21.42 | 617.9 | 100.2 | 41 |
| Aden | 113.0 | 21.36 | 1251.4 | 99.1 | 34 |
| Ida | 114.0 | 21.39 | 1872.5 | 99.1 | 24 |

## Extraction parameters

- **grayscale_command:** convert bin2015-fig-0001-m.jpg -colorspace Gray -depth 8 fig_gray.pgm
- **black_pixel_threshold:** gray < 90 for marker/line sampling
- **gray_bar_pixel_threshold:** 120 < gray < 230 for correct-answer bars
- **gray_bar_component_filter:** vertical segment height > 35 px, component width >= 5 px, bottom within 20 px of panel x-axis
- **set1_marker_filter:** 15x15 sampling window at calibrated session x response y intersections; black-pixel density threshold >= 45; then visual QA/manual correction for triangle overlap and axis/tick false positives
- **set2_marker_filter:** manual QA from isolated black triangle symbols after affine calibration; values snapped to nearest integer count 0-5
- **rounding_rule:** all response values snapped to nearest integer in [0,5]

## Output files

- `swensson_figure1_digitized_marks.csv`: mark-level digitization, one row per extracted square/triangle/bar.
- `swensson_figure1_session_carriers.csv`: session-level EB carrier table using Set 1 and correct-answer values.
- `swensson_figure1_eb_summary.csv`: phase-level summaries of K, I, A, and R.
- `swensson_figure1_digitization_calibration.json`: machine-readable calibration and parameter settings.

## EB carrier definitions

- `K_correct_answers` = digitized correct-answer count.
- `I_idkptm_set1` = digitized IDKPTM Set 1 count.
- `G_idkptm_set2_generalization` = digitized IDKPTM Set 2/generalization probe count.
- `L_t_carrier = (K,I)`.
- `A_naive_K_plus_I = K + I`.
- `A_capped_min5 = min(5, K + I)`.
- `overflow_K_plus_I_minus5 = max(0, K + I - 5)`, retained as a possible overlap/digitization flag.
- `R_residual_5_minus_Acapped = 5 - A_capped`.

## QA notes

- This is a digitized reconstruction from the published figure, not author-provided raw data.
- Black square Set 1 values were visually QA-corrected where triangle probes or x-axis ticks overlapped the sampling window.
- Set 2 triangle probes are sparse and were manually digitized; sessions are approximate to the nearest x-axis tick.
- Correct-answer bars were automatically extracted and snapped to integer response values; very late Alex bars are lower confidence because bars and final Set 1 markers overlap near the right edge.

## Phase summary

| Participant | Phase | n | mean K | mean I | mean A capped | mean R | overflow sessions |
|---|---|---:|---:|---:|---:|---:|---:|
| Alex | BL | 5 | 0 | 0.0 | 0.0 | 5.0 | 0 |
| Alex | Intervention_10_targets | 32 | 1.583 | 2.906 | 4.094 | 0.906 | 0 |
| Alex | Intervention_5_targets | 22 | 1.667 | 1.636 | 3.227 | 1.773 | 0 |
| Alex | Teaching | 2 | 0 | 0.0 | 0.0 | 5.0 | 0 |
| Aden | BL | 9 | 0 | 0.0 | 0.0 | 5.0 | 0 |
| Aden | Intervention_10_targets | 24 | 1.667 | 3.792 | 4.625 | 0.375 | 0 |
| Aden | Intervention_5_targets | 6 | 2.0 | 1.167 | 3.167 | 1.833 | 0 |
| Ida | BL | 13 | 1.0 | 0.0 | 0.308 | 4.692 | 0 |
| Ida | Intervention_10_targets | 10 | 1.4 | 1.5 | 2.9 | 2.1 | 0 |
| Ida | Intervention_5_targets | 3 | 4.667 | 0.0 | 4.667 | 0.333 | 0 |
