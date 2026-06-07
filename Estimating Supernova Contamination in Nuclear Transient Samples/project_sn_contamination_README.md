# Estimating Supernova Contamination in Nuclear Transient Samples Using Spatial Offset Distributions

**Course:** Statistics and Data Analysis at Leiden University  
**Date:** May 2025

---

## Overview

Wide-field surveys like the Zwicky Transient Facility (ZTF) detect thousands of extragalactic transients per year. Identifying rare tidal disruption events (TDEs), which is where a star is shredded by a supermassive black hole, often relies on selecting sources that appear close to the centres of their host galaxies ("nuclear transients"). However, supernovae (SNe) can also appear near galactic centres due to projection effects or central star formation, contaminating TDE samples and biasing population studies.

This project builds a statistical mixture model to quantify what fraction of unclassified ZTF nuclear transients are likely supernovae, using spatial offset distributions alone.

## Research Question

> What fraction of unclassified nuclear transients are likely supernovae based on spatial offset alone?

## Methods

**Dataset (ZTF)**
- AGN: 375 events (known nuclear sources)
- SNe: 198 events (known supernovae)
- Unknown: 1139 unclassified nuclear transients
- Extreme outliers (r > 5″) excluded for numerical stability.

**Kolmogorov-Smirnov Tests**  
Confirmed statistically significant differences between the unknown sample and both labeled classes (Unknown vs. AGN: D = 0.427, p < 0.0001; Unknown vs. SN: D = 0.195, p = 0.005).

**Nuclear Offset Model**  
AGN offsets modelled as a 2D Gaussian centred at zero (offsets due to astrometric error only). MLE fit to AGN data yields σ̂ₓᵧ = 0.1307 arcsec (95% CI: 0.1218–0.1393).

**SN Offset Model**  
Gaussian kernel density estimation (KDE) applied to empirical SN offset data to construct a smooth probability density, with bandwidth selected to balance bias and variance.

**Mixture Model + MLE**  
Unknown distribution modelled as a linear combination:

P(r) = f_nuc · P_nuc(r) + (1 − f_nuc) · P_SN(r)

MLE fit to unknown offsets. Bootstrap 95% confidence intervals computed for all parameters.

**Joint Fit**  
Extended model simultaneously fitting both f_nuc and σₓᵧ as free parameters, to account for variability in astrometric precision across individual sources.

## Key Results

| Model | f_nuc (nuclear fraction) | f_SN (SN fraction) |
|---|---|---|
| Fixed σ MLE | 0.248 (CI: 0.164–0.426) | 0.752 (CI: 0.574–0.836) |
| Joint MLE (σ free) | 0.556 (CI: 0.277–0.856) | 0.444 (CI: 0.193–0.691) |

- The 90% confidence radius r₉₀ = 0.2806 arcsec; within this radius, ~51% of unknowns are estimated to be SNe (fixed model), confirming that even strict nuclear selection cannot eliminate SN contamination.
- The joint fit yields broader confidence intervals, reflecting realistic variability in astrometric precision. It reinforces the conclusion that spatial offset alone is insufficient for clean TDE selection.

## Conclusions

Spatial offset is not sufficient as a sole criterion for distinguishing TDEs from supernovae in nuclear transient samples. Future surveys and classification pipelines should incorporate additional features like light curve shape, colour evolution, host galaxy properties and/or multi-wavelength data, alongside machine learning methods to achieve higher sample purity.

## Tools & Libraries

- Python, NumPy, SciPy, Matplotlib
- `scipy.stats` (KS tests, MLE optimisation)
- Gaussian KDE (SN offset modelling)
- Bootstrap resampling (confidence intervals)
- LaTeX (report)

## Files

| File | Description |
|---|---|
| `report.pdf` | Full written report with figures and statistical derivations |
| `code/mixture_model.py` | Mixture model, MLE fitting, and bootstrap CI |
| `code/kde_model.py` | Gaussian KDE for SN offset distribution |
