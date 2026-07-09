# ============================================================
# Internal Debt and Indian Macroeconomic Variables
# Econometric Analysis
# Author: Lakshita Guptaa
# Institution: Christ University, Bengaluru
# ============================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, coint
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from statsmodels.stats.stattools import durbin_watson
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
df = pd.read_csv('data.csv', parse_dates=['Year'], index_col='Year')
print("Data loaded successfully.")
print(df.head())
print(f"\nShape: {df.shape}")
print(f"\nDescriptive Statistics:\n{df.describe()}")

# ─────────────────────────────────────────────
# 2. ADF UNIT ROOT TEST
# ─────────────────────────────────────────────
def adf_test(series, name):
    result = adfuller(series.dropna(), autolag='AIC')
    print(f"\nADF Test — {name}")
    print(f"  Test Statistic : {result[0]:.4f}")
    print(f"  p-value        : {result[1]:.4f}")
    print(f"  Lags Used      : {result[2]}")
    for key, val in result[4].items():
        print(f"  Critical Value ({key}): {val:.4f}")
    if result[1] < 0.05:
        print(f"  → Stationary at 5% significance level")
    else:
        print(f"  → Non-stationary (unit root present)")

print("\n" + "="*50)
print("UNIT ROOT TESTS (LEVEL)")
print("="*50)
for col in df.columns:
    adf_test(df[col], col)

print("\n" + "="*50)
print("UNIT ROOT TESTS (FIRST DIFFERENCE)")
print("="*50)
for col in df.columns:
    adf_test(df[col].diff(), f"Δ{col}")

# ─────────────────────────────────────────────
# 3. JOHANSEN COINTEGRATION TEST
# ─────────────────────────────────────────────
print("\n" + "="*50)
print("JOHANSEN COINTEGRATION TEST")
print("="*50)

clean_df = df.dropna()
johansen_result = coint_johansen(clean_df, det_order=0, k_ar_diff=1)

print("\nTrace Statistic:")
for i, (trace, cv) in enumerate(zip(johansen_result.lr1, johansen_result.cvt[:, 1])):
    print(f"  r <= {i}: Trace = {trace:.4f}, Critical Value (5%) = {cv:.4f}", 
          "→ Reject H0" if trace > cv else "→ Fail to Reject H0")

print("\nMax Eigenvalue Statistic:")
for i, (maxeig, cv) in enumerate(zip(johansen_result.lr2, johansen_result.cvm[:, 1])):
    print(f"  r <= {i}: Max-Eig = {maxeig:.4f}, Critical Value (5%) = {cv:.4f}",
          "→ Reject H0" if maxeig > cv else "→ Fail to Reject H0")

# ─────────────────────────────────────────────
# 4. OLS REGRESSION
#    Dependent: GDP Growth Rate
#    Independent: Internal Debt (% of GDP), Inflation, Fiscal Deficit
# ─────────────────────────────────────────────
print("\n" + "="*50)
print("OLS REGRESSION")
print("="*50)

y = df['GDP_Growth']
X = df[['Internal_Debt_GDP', 'Inflation', 'Fiscal_Deficit_GDP']]
X = sm.add_constant(X)
clean = pd.concat([y, X], axis=1).dropna()

model = sm.OLS(clean['GDP_Growth'], clean[['const', 'Internal_Debt_GDP', 'Inflation', 'Fiscal_Deficit_GDP']])
results = model.fit()
print(results.summary())

dw = durbin_watson(results.resid)
print(f"\nDurbin-Watson Statistic: {dw:.4f}")
if 1.5 < dw < 2.5:
    print("→ No significant autocorrelation in residuals")
else:
    print("→ Potential autocorrelation detected")

# ─────────────────────────────────────────────
# 5. PLOTS
# ─────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Internal Debt & Indian Macroeconomic Variables", fontsize=14, fontweight='bold')

df['Internal_Debt_GDP'].plot(ax=axes[0,0], color='steelblue', marker='o', linewidth=2)
axes[0,0].set_title("Internal Debt (% of GDP)")
axes[0,0].set_ylabel("% of GDP")

df['GDP_Growth'].plot(ax=axes[0,1], color='green', marker='s', linewidth=2)
axes[0,1].set_title("GDP Growth Rate (%)")
axes[0,1].set_ylabel("%")

df['Inflation'].plot(ax=axes[1,0], color='tomato', marker='^', linewidth=2)
axes[1,0].set_title("Inflation Rate (WPI, %)")
axes[1,0].set_ylabel("%")

df['Fiscal_Deficit_GDP'].plot(ax=axes[1,1], color='purple', marker='D', linewidth=2)
axes[1,1].set_title("Fiscal Deficit (% of GDP)")
axes[1,1].set_ylabel("% of GDP")

plt.tight_layout()
plt.savefig('macro_trends.png', dpi=150)
print("\nPlot saved as 'macro_trends.png'")

# Residual plot
fig2, ax = plt.subplots(figsize=(10, 4))
results.resid.plot(ax=ax, color='darkred')
ax.axhline(0, color='black', linestyle='--')
ax.set_title("OLS Residuals")
plt.tight_layout()
plt.savefig('residuals.png', dpi=150)
print("Residual plot saved as 'residuals.png'")

print("\n✓ Analysis complete.")
