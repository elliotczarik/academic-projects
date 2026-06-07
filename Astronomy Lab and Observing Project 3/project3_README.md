# Characterisation of the Hot Jupiter TOI-163b

**Course:** Astronomy Lab & Observing Project 3 — Leiden University  
**Team:** Thijn Kriesels, Tim Dinh, Reinier Barendregt, Muhamed Hameed, Elliot Czarik, Yentl Fonteyn  
**Date:** May 2026

---

## Overview

This team project aimed to constrain the physical and orbital properties of TOI-163b, a known exoplanet candidate, by combining two independent observational techniques: space-based photometric transit observations from TESS and ground-based radial velocity (RV) measurements from the FEROS spectrograph. Our results confirm TOI-163b as an inflated hot Jupiter with a low bulk density, consistent with thermal inflation models.

## Scientific Questions

- Can combining TESS transit photometry and FEROS RV data provide tight constraints on the bulk density of TOI-163b?
- Does the planet's low density independently confirm it as an inflated hot Jupiter?
- How do our derived parameters compare to those in the discovery paper (Kossakowski et al. 2019)?

## Methods

**Transit Photometry (TESS)**  
Selected the shortest available cadence from each TESS sector. Preprocessed light curves (flattening, outlier removal, transit masking). Modelled transits with BATMAN using a quadratic limb-darkening model; parameter uncertainties estimated via MCMC.

**Radial Velocity (FEROS)**  
Fitted RV data using Juliet, assuming a single-planet Keplerian model. Fit favours this model with likelihood ratio > 200:1 over a no-planet null hypothesis. The phased RV curve forms a near-perfect sine wave consistent with near-zero eccentricity.

## Key Results

| Parameter | This Work | Kossakowski et al. (2019) |
|---|---|---|
| Orbital Period (Transit) | 4.23112558 ± 0.00000006 days | 4.231306 ± 0.000063 days |
| Orbital Period (RV) | 4.217 ± 0.021 days | 4.231 ± 0.063 days |
| Planet Radius R_p | 1.342 ± 0.019 R_J | 1.489 ± 0.034 R_J |
| Planet Mass M_p | 1.207 ± 0.028 M_J | 1.22 ± 0.12 M_J |
| Eccentricity e | 0.046 ± 0.044 | 0 (fixed) |
| Inclination i | 87.13 ± 0.17° | 87.24 ± 0.47° |
| Average Density ρ | 0.621 ± 0.041 g/cm³ | 0.490 ± 0.055 g/cm³ |

- The derived low bulk density (ρ ≈ 0.46 ρ_Jup) independently confirms TOI-163b as an inflated hot Jupiter.
- Our transit measurements favour a slightly smaller planetary radius than the discovery paper, with better constrained uncertainties.
- Results suggest TOI-163b is an interesting candidate for follow-up transmission spectroscopy.

## Tools & Libraries

- Python, NumPy, Matplotlib
- BATMAN (transit light curve modelling)
- Juliet (RV + transit joint fitting)
- MCMC (parameter uncertainty estimation)
- LaTeX / academic poster format

## Files

| File | Description |
|---|---|
| `poster.pdf` | Final project poster (Leiden University, May 2026) |
| `code/transit_fit.py` | TESS transit modelling with BATMAN |
| `code/rv_fit.py` | FEROS RV fitting with Juliet |

## Reference

Kossakowski et al. 2019, *Monthly Notices of the Royal Astronomical Society*, 490, 1094–1110. https://doi.org/10.1093/mnras/stz2433
