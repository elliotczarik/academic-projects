# UBV Photometric Analysis of Stellar Populations

**Course:** Astronomy Lab & Observing Project at Leiden University  
**Date:** October 2025

---

## Overview

This project investigates the relationship between stellar colors, spectral types, and atmospheric physics using UBV photometry. The analysis has two parts: synthetic photometry on a reference spectral library, and aperture photometry on real CCD images.

## Scientific Questions

- How do stellar colors relate to spectral type and effective temperature?
- How and why do real stellar spectra deviate from blackbody predictions?
- Can photometric colors alone be used to classify stars and estimate their distances?

## Methods

**Synthetic Photometry**  
Computed UBV magnitudes for a reference library of stellar spectra spanning O5 to M8 (main sequence and giants) using top-hat filter approximations and trapezoidal integration. Calibrated against the Vega spectrum.

**Blackbody Comparison**  
For four spectral types (B0V, A0V, F2V, G0V), found the blackbody temperature producing the same B−V color as each star and compared the flux ratios wavelength by wavelength.

**CCD Aperture Photometry**  
Processed B and V band CCD images using a 5σ source detection algorithm and circular aperture photometry (r = 5 px, sky annulus 8–12 px). Computed signal-to-noise ratios and photometric uncertainties for 26 detected sources.

**Spectroscopic Parallax**  
Estimated distances for 5 high-quality detections (S/N > 5) by matching observed B−V colors to spectral type standards and applying the distance modulus.

## Key Results

- The U−B vs B−V color-color diagram clearly separates main sequence and giant stars, and both populations deviate systematically from blackbody predictions.
- A-type stars show ~50% flux deficit shortward of the Balmer discontinuity (3646 Å) in the U band. Cooler stars show 10–30% deficits from metal line blanketing.
- 5 stars with reliable photometry span spectral types A1V–G5V, at distances of 39–601 pc.
- Photometric distance precision is ~20%, compared to ~0.1–6% achievable with Gaia parallaxes over the same range.

## Tools & Libraries

- Python, NumPy, SciPy, Matplotlib
- Astropy (unit handling)
- LaTeX (report)

## Files

| File | Description |
|---|---|
| `report.pdf` | Full written report |
| `code/photometry.py` | Synthetic photometry and blackbody comparison |
| `code/ccd_reduction.py` | Aperture photometry pipeline |
