# Swensson Figure 1 digitization correction log v3

## Correction scope

Rechecked Alex late-phase sessions using a calibrated overlay grid on the high-resolution Figure 1 image. The prior digitized CSV under-detected late gray correct-answer bars, especially sessions 55-62. This file patches the affected Alex rows and adds confidence/notes columns.

## Calibration used

- Source image: `/mnt/data/bin2015-fig-0001-m.jpg`
- Alex panel calibration: x0 = 113.5 px at session 0; x step = 21.42 px/session; y0 = 617.9 px at response 0; y step = 100.2 px/response.
- Values snapped to integer response counts 0-5.
- Manual QA region: Alex sessions 48-62, with strongest correction at sessions 55-62.

## Patched rows

| child | session | idkptm_set1 | correct | confidence | note |
|---|---:|---:|---:|---|---|
| Alex | 48 | 2 | 3 | medium | Recovered black square near y=2 and gray bar near y=3 in calibrated overlay. |
| Alex | 49 | 1 | 4 | medium | Gray bar reaches y=4; black square near y=1. |
| Alex | 51 | 1 | 3 | medium | Gray bar visible near y=3 behind line; prior CSV missed bar. |
| Alex | 52 | 1 | 1 | medium | Small gray bar near y=1; black square near y=1. |
| Alex | 53 | 2 | 3 | medium | Recovered black square near y=2 and gray bar near y=3. |
| Alex | 55 | 1 | 4 | high | Late-phase gray bar reaches y=4; black square near y=1. |
| Alex | 56 | 2 | 3 | high | Late-phase gray bar reaches y=3; black square near y=2. |
| Alex | 57 | 3 | 1 | medium | Black square near y=3; correct bar appears small near y=1; avoided impossible sum from automated gray pass. |
| Alex | 58 | 1 | 4 | high | Late-phase gray bar reaches y=4; black square near y=1. |
| Alex | 59 | 2 | 3 | high | Late-phase gray bar reaches y=3; black square near y=2. |
| Alex | 60 | 0 | 5 | high | Mastery sequence bar reaches y=5; black square at y=0. |
| Alex | 61 | 0 | 4 | high | Mastery sequence bar reaches y=4; black square at y=0. |
| Alex | 62 | 1 | 4 | high | Final gray bar reaches y=4; black square near y=1. |

## Corrected Set 1 intervention slack summary

| child | n | mean slack | zero-slack sessions | max slack | mean IDKPTM | mean correct |
|---|---:|---:|---:|---:|---:|---:|
| Alex | 50 | 0.84 | 25/50 (50.0%) | 5 | 2.34 | 1.82 |
| Aden | 28 | 0.107 | 25/28 (89.3%) | 1 | 3.25 | 1.643 |
| Ida | 14 | 1.071 | 6/14 (42.9%) | 4 | 0.929 | 3.0 |
