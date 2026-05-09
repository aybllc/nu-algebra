# Swensson et al. (2024) Validation with SAID Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation: CC-BY-4.0](https://img.shields.io/badge/Docs-CC--BY--4.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

**Self-Amending Iterative Documentation (SAID) in practice**

## Overview

This repository demonstrates the SAID framework applied to validation of Swensson et al. (2024) IoA (Interval of Agreement) methodology for Hubble constant uncertainty analysis.

**Key demonstration**: How to document, correct, and learn from scientific errors systematically.

## Quick Links

- **Current Analysis**: [`manuscript_v2.md`](manuscript_v2.md) (v2.0 - corrected)
- **Error Timeline**: [`SAID/version_history.md`](SAID/version_history.md)
- **Framework Docs**: [`SAID/README.md`](SAID/README.md)
- **Validation Scripts**: [`SAID/validation_data/`](SAID/validation_data/)

## What Happened

### v1.0 (December 2024) ❌ DEPRECATED
- Applied N/U algebra to IoA data
- **Error**: Attempted temporal gap analysis (out of scope)
- **Category confusion**: Used measurement tool for inference

### v1.1 (January 2025) ✓ Correction Initiated
- **Discovery**: 48hr temporal separation + computational review
- **Action**: Error acknowledged, stakeholders notified
- **Framework**: SAID process caught category error

### v2.0 (October 2025) ✅ CURRENT
- **Correction**: Restricted N/U algebra to measurement propagation
- **Validation**: α = +0.994 confirmed from SH0ES Cepheid data
- **Added**: Methodological addendum explaining scope limits

## Repository Structure

```
swensson_validation/
├── README.md (this file)
├── manuscript_v2.md                  # Current corrected analysis
├── SAID/                             # Self-amending documentation
│   ├── README.md                     # Framework overview
│   ├── version_history.md            # Timeline of changes
│   ├── version_history/              # Detailed version docs
│   │   ├── v1_initial_analysis.md    # Original error (deprecated)
│   │   ├── error_recognition.md      # Discovery process
│   │   └── v2_correction.md          # Corrected analysis
│   ├── email_correspondence/         # Communication audit
│   └── validation_data/              # Cross-validation scripts
│       ├── cross_validation_cepheid.py
│       └── ioa_conversion_test.py
├── data/
│   └── swensson_2024_table1.csv      # Source data
└── analysis/
    ├── v1_gap_analysis.py (deprecated)
    └── v2_measurement_propagation.py (current)
```

## Running Validation

### Prerequisites
```bash
# Python 3.10+
pip install numpy pandas scipy matplotlib
```

### Cross-Validation Test
```bash
cd SAID/validation_data
python cross_validation_cepheid.py
```

**Expected output:**
```
✅ α ≈ +0.994 confirmed from LMC anchor
✅ Factor analysis matches SH0ES inverse variances
```

## SAID Framework Principles

This repository demonstrates:

1. **✅ Transparent Error Documentation**
   - All versions preserved with timestamps
   - Errors acknowledged publicly, not hidden
   
2. **✅ Version Control Provenance**
   - Git hashes link analysis to exact code states
   - Reproducibility at every stage
   
3. **✅ Communication Audit Trail**
   - Email correspondence archived
   - Stakeholder notifications documented
   
4. **✅ Temporal Separation**
   - 24-48hr forced review delays
   - Catches confirmation bias and category errors
   
5. **✅ Self-Correction Timeline**
   - Process visible to scientific community
   - Learning captured for future work

## Key Lessons

### For Researchers
- **Layer discipline**: Measurement tools ≠ inference tools
- **Scope clarity**: State what method CAN'T do, not just what it can
- **Temporal separation works**: 48hr delays catch errors
- **SAID value**: Framework makes correction systematic, not ad-hoc

### For Institutions
- **Error normalization**: Mistakes become teaching moments
- **Junior training**: See how seniors handle corrections
- **Reproducibility default**: Process + code + data in git
- **Publication standard**: SAID/ could be required for journals

## The Bigger Vision

### SAID as Standard Practice

**Imagine if journals required:**
```
Submission checklist:
☐ Manuscript PDF
☐ Data files
☐ Analysis code
☐ SAID/ directory (version history, corrections, process docs)
```

**Benefits:**
- Pre-registration with teeth
- Reproducibility by default  
- Negative results cannot be hidden
- Institutional learning accumulates
- Complete provenance (L6 hashes + Git + SAID)

## Citation

If you use or reference this work:

```bibtex
@misc{swensson_validation_2025,
  title = {Swensson et al. (2024) Validation with SAID Framework},
  author = {[Your Name]},
  year = {2025},
  howpublished = {\url{https://github.com/[org]/swensson_validation}},
  note = {Demonstrates Self-Amending Iterative Documentation}
}
```

## License

- **Documentation** (SAID/, README, manuscript): CC-BY-4.0
- **Code** (analysis/, validation scripts): MIT

## Contact

- **Primary**: [email]
- **Issues**: Use GitHub issues for questions
- **Collaboration**: PRs welcome for validation scripts

---

*"Science self-corrects, but only if corrections are visible."*

*Built with the Seven-Layer Methodology and N/U Algebra*
