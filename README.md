# Academic Portfolio — Elliot Czarik

BSc Astronomy student at Leiden University, with a Minor in Biomedical Engineering at TU Delft. This repository collects the reports, code, and data analysis work from my undergraduate research projects, spanning exoplanet characterisation, stellar photometry, and biomedical instrumentation.

📧 elliotczarik@gmail.com · [LinkedIn](https://www.linkedin.com/in/elliot-czarik) · Leiden, Netherlands

---

## Projects

### Astronomy & Astrophysics — Leiden University

| Project | Description | Tools | Report | Code |
|---|---|---|---|---|
| [UBV Photometric Analysis of Stellar Populations](#) | Synthetic photometry on a reference spectral library (O5–M8), construction of U−B vs B−V color-color diagrams, and CCD aperture photometry of 26 field stars. Characterised deviations from blackbody emission (Balmer discontinuity, metal line blanketing) and estimated stellar distances via spectroscopic parallax. | Python, NumPy, Matplotlib | [Report](#) | [Code](#) |
| [Radial Velocity Characterisation of 51 Pegasi b](#) | Independent re-analysis of the Mayor & Queloz (1995) discovery dataset for the first confirmed exoplanet around a main-sequence star. Derived orbital parameters using χ² grid-search minimisation and Bayesian MCMC sampling (emcee), recovering a minimum planetary mass of M_p sin i = 0.483 ± 0.006 M_J (reduced χ² = 1.048). | Python, NumPy, emcee, Matplotlib | [Report](#) | [Code](#) |
| [Characterisation of the Hot Jupiter TOI-163b](#) | Team project combining space-based TESS photometric transit data with ground-based FEROS radial velocity measurements to constrain the bulk density and orbital parameters of TOI-163b. Transit modelling performed with BATMAN; RV fitting with Juliet. Confirmed the planet as an inflated hot Jupiter (ρ = 0.62 ± 0.04 g/cm³, P = 4.22 ± 0.02 days). | Python, BATMAN, Juliet, MCMC | [Poster](#) | [Code](#) |
| [Estimating Supernova Contamination in Nuclear Transient Samples](#) | Statistical analysis of ZTF spatial offset data (1,712 transients across AGN, SNe, and unknowns) to quantify supernova contamination in nuclear transient samples. Built a mixture model combining a Gaussian nuclear offset model (MLE-fitted) and Gaussian KDE for SNe, finding ~75% of unclassified nuclear transients are likely supernovae. Joint MLE fit simultaneously constrained the nuclear fraction and astrometric uncertainty. | Python, NumPy, SciPy, KDE, Bootstrap | [Report](#) | [Code](#) |

### Biomedical Engineering Minor — TU Delft

| Project | Description | Tools | Report | Code |
|---|---|---|---|---|
| [Mechanical Characterisation of a Surgical Endo Pouch](#) | Team project developing a four-test mechanical safety battery for a novel laparoscopic tissue containment device. Designed and 3D-printed custom test rigs in SolidWorks; executed insertion and extraction force tests across clinically relevant trocar sizes (8–15 mm) and incision diameters (10–24 mm). Key finding: incisions ≥18 mm and trocars ≥12 mm ensure safe, low-force operation. | SolidWorks, PMMA/ABS fabrication, force measurement | [Report](#) | — |

---

## Skills Demonstrated

**Data Analysis & Statistics** — χ² minimisation, Bayesian inference, MCMC sampling, maximum likelihood estimation, kernel density estimation, bootstrap confidence intervals, hypothesis testing (KS tests), signal-to-noise analysis, error propagation

**Astronomical Techniques** — Aperture photometry, radial velocity analysis, transit photometry, spectroscopic parallax, light curve modelling, mixture modelling for transient classification

**Biomedical Engineering** — Mechanical test design, SolidWorks CAD, 3D printing (ABS/PMMA), force measurement, medical device safety characterisation

**Programming** — Python (NumPy, SciPy, Matplotlib, Astropy, emcee, BATMAN, Juliet), LaTeX, SolidWorks

---

## Repository Structure

```
academic-projects/
├── photometric-analysis-stellar-populations/
│   ├── README.md
│   ├── report.pdf
│   └── code/
├── radial-velocity-51-pegasi-b/
│   ├── README.md
│   ├── report.pdf
│   └── code/
├── toi-163b-characterisation/
│   ├── README.md
│   ├── poster.pdf
│   └── code/
├── supernova-contamination-nuclear-transients/
│   ├── README.md
│   ├── report.pdf
│   └── code/
└── surgical-endo-pouch-mechanical-characterisation/
    ├── README.md
    └── report.pdf
```

---

*All reports and code are shared for educational purposes. Please cite appropriately if you build on this work.*
