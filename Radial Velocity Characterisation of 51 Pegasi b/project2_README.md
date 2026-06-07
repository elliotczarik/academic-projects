# Radial Velocity Characterisation of 51 Pegasi b

**Course:** Astronomy Lab & Observing Project at Leiden University  
**Date:** January 2026

---

## Overview

An independent re-analysis of the original Mayor & Queloz (1995) radial velocity dataset for 51 Pegasi. 51 Pegasi is the star hosting the first confirmed exoplanet around a main-sequence star, a discovery that earned the 2019 Nobel Prize in Physics. Using two complementary fitting approaches, I recovered the orbital parameters and minimum planetary mass of 51 Peg b from scratch.

## Scientific Questions

- What radial velocity amplitudes do solar system planets induce on the Sun, and how does this compare to 51 Peg b?
- Can a simple sinusoidal model statistically describe the observed radial velocity variations?
- How do χ² minimisation and Bayesian MCMC compare in parameter estimation and uncertainty quantification?
- What is the minimum mass of 51 Peg b, and how precisely can it be determined from the original data?

## Methods

**χ² Grid Search Minimisation**  
Two-stage grid search (coarse then fine) over four parameters: semi-amplitude K, orbital period P, phase offset f₀, and systemic velocity v₀. Best-fit parameters confirmed with formal goodness-of-fit testing at 95% confidence.

**Bayesian MCMC Sampling**  
32 walkers run for 5000 steps using `emcee`, with 1000-step burn-in, yielding 128,000 posterior samples. Gaussian priors centred on χ² best-fit values. Parameter estimates and uncertainties taken from 16th/50th/84th posterior percentiles.

**Planetary Mass Derivation**  
Minimum mass M_p sin i derived analytically from K and P, with uncertainties propagated through all MCMC samples to capture parameter correlations.

## Key Results

| Parameter | This Work | Mayor & Queloz (1995) |
|---|---|---|
| Orbital Period P | 4.2331 ± 0.0010 days | 4.229 ± 0.001 days |
| Semi-amplitude K | 56.59 ± 0.67 m/s | 55.94 ± 0.69 m/s |
| Min. Planetary Mass M_p sin i | 0.483 ± 0.006 M_J | 0.47 ± 0.02 M_J |
| Reduced χ² | 1.048 | — |

- Both methods converge to consistent parameter values, validating the sinusoidal model.
- The model cannot be rejected at 95% confidence (χ²_best = 76.48 < χ²_lim = 93.95).
- MCMC corner plot reveals only weak correlations between parameters (strongest: P and f₀, r ≈ 0.3), indicating robust constraints.
- Results are in excellent agreement with the original discovery paper and modern re-analyses (Fischer et al. 2014).

## Tools & Libraries

- Python, NumPy, SciPy, Matplotlib
- emcee (MCMC sampling)
- corner (posterior visualisation)
- LaTeX (report)

## Files

| File | Description |
|---|---|
| `report.pdf` | Full written report with figures |
| `code/chi2_fit.py` | Grid-search χ² minimisation |
| `code/mcmc_fit.py` | Bayesian MCMC analysis with emcee |
| `data/mayor_queloz_1995.dat` | Original RV dataset |
