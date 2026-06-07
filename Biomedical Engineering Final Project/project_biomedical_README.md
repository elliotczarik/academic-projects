# Mechanical Characterisation of a Surgical Endo Pouch

**Course:** Biomedical Engineering Minor — TU Delft  
**Team:** Tony Euwals, Elliot Czarik, Elvira Zonneveld, Geert Wormgoor, Jibiao Zhang  
**Supervised by:** Dr. Johann Rhemrev, Dr. Jim English, Prof. dr. John van den Dobbelsteen  
**Date:** 2026

---

## Overview

During laparoscopic morcellation procedures (e.g. myomectomies, hysterectomies), tissue is broken into fragments inside a surgical endo pouch to prevent the spread of potentially malignant cells. If the pouch tears or ruptures during the procedure, containment is lost — with serious consequences for the patient. This project developed and executed a mechanical test battery to characterise the safety and durability of a newly designed endo pouch prototype across four critical phases of its use.

## Research Questions

- For different clinically relevant incision sizes, how much force is required to extract the endo pouch for varying masses of contained tissue?
- For different clinically relevant trocar sizes, how much force is required to insert the endo pouch?

## Test Design

Four distinct tests were designed, each targeting a specific failure mode:

| Test | Phase | Failure Mode | Status |
|---|---|---|---|
| Extraction test | Post-morcellation extraction | Bag tearing from excessive force | ✅ Executed |
| Insertion test | Trocar insertion | Bag tearing from excessive force | ✅ Executed |
| Puncture test | Tissue manipulation | Bag puncture from sharp instrument | ⚠️ Protocol designed; not executed (equipment/time) |
| Burst test | CO₂ insufflation | Bag rupture from over-pressurisation | ⚠️ Protocol designed; not executed (equipment/time) |

**Test rigs** were custom-designed in SolidWorks and fabricated from PMMA (extraction board) and 3D-printed ABS (insertion board), with trocar diameters of 8–15 mm and incision sizes of 10–24 mm. Chicken fillet with blue food dye was used as tissue phantom; forces were measured with a calibrated digital scale and converted via F = mg.

## Key Results

### Extraction Test
- Three distinct performance zones identified across hole sizes 10–24 mm and tissue loads 5–35 g:
  - **≥22 mm**: minimal force (3.9–7.0 N), 100% success across all tissue amounts
  - **16–20 mm**: moderate forces (5.3–22.3 N), complete success
  - **<16 mm**: progressive failures; 10 mm hole failed at ≥10 g tissue with max recorded force 32.0 ± 4.9 N
- No leakage or pouch failure occurred during any trial.
- **Recommendation:** minimum incision size of 18 mm for reliable extraction; 22–24 mm for optimal performance.

### Insertion Test
- Strong inverse relationship between trocar diameter and insertion force:

| Trocar Size | Mean Force |
|---|---|
| 10 mm | 71.4 ± 9.43 N |
| 11 mm | 24.4 ± 1.95 N |
| 12 mm | 15.19 ± 3.29 N |
| 15 mm | 6.69 ± 3.29 N |

- 8 mm configuration exceeded measurement threshold and became stuck, suggesting a critical lower mechanical limit.
- **Recommendation:** trocar size ≥12 mm for a favourable balance of insertion force and procedural consistency.

## Tools & Methods

- SolidWorks (custom test rig design)
- PMMA and ABS 3D-printed mechanical test fixtures
- Digital electronic scale with F = mg force conversion
- Statistical analysis: mean ± standard deviation across 5 trials per condition

## Limitations

- Chicken fillet is considerably softer than clinical tissue (uterine fibroids, myomas) — forces may underestimate real-world requirements.
- Manual bag rolling for insertion tests introduced operator-dependent variability.
- Extraction test could not be performed by a single operator throughout, introducing additional measurement error.
- Puncture and burst tests remain unexecuted; full mechanical safety characterisation requires further work.

## Files

| File | Description |
|---|---|
| `report.pdf` | Full written report with results, figures, and discussion |
