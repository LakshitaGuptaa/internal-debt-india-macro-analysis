# Internal Debt and Indian Macroeconomic Variables

> Econometric analysis examining the relationship between internal debt and key macroeconomic indicators in India (2000–2023)

**Author:** Lakshita Guptaa  
**Institution:** Christ University, Bengaluru  
**Program:** B.A. (Hons.) Economics  

---

## 📌 Overview

This study investigates the dynamic relationship between India's internal debt (as a percentage of GDP) and macroeconomic variables including GDP growth rate, inflation, and fiscal deficit. The analysis employs time-series econometric techniques to test for stationarity, long-run cointegration, and causal relationships between the variables.

---

## 🔬 Methodology

| Technique | Purpose |
|---|---|
| ADF Unit Root Test | Test for stationarity in levels and first differences |
| Johansen Cointegration Test | Identify long-run equilibrium relationships |
| OLS Regression | Estimate magnitude and direction of impact |
| Durbin-Watson Test | Detect autocorrelation in residuals |

---

## 📁 Repository Structure

```
internal-debt-india-macro-analysis/
│
├── analysis.py       # Main econometric analysis script
├── data.csv          # Annual macroeconomic data (2000–2023)
├── README.md         # Project documentation
```

---

## 📊 Variables

| Variable | Description | Source |
|---|---|---|
| `Internal_Debt_GDP` | Internal debt as % of GDP | RBI Handbook of Statistics |
| `GDP_Growth` | Real GDP growth rate (%) | World Bank / MOSPI |
| `Inflation` | WPI-based inflation rate (%) | Office of the Economic Adviser |
| `Fiscal_Deficit_GDP` | Fiscal deficit as % of GDP | Union Budget Documents |

---

## ⚙️ Requirements

```bash
pip install pandas numpy statsmodels matplotlib
```

---

## ▶️ How to Run

```bash
git clone https://github.com/LakshitaGuptaa/internal-debt-india-macro-analysis.git
cd internal-debt-india-macro-analysis
pip install pandas numpy statsmodels matplotlib
python analysis.py
```

---

## 📈 Key Findings

- Internal debt in India showed an upward trend, accelerating post-2019 due to pandemic-related fiscal expansion
- ADF tests indicate variables are integrated of order I(1), satisfying conditions for cointegration analysis
- Johansen test reveals evidence of a long-run cointegrating relationship between internal debt and GDP growth
- OLS results indicate a statistically significant negative association between rising internal debt ratios and GDP growth

---

## 📝 Citation

If referencing this work:
```
Guptaa, L. (2026). Internal Debt and Indian Macroeconomic Variables: An Econometric Analysis.
B.A. (Hons.) Economics Dissertation, Christ University, Bengaluru.
```
