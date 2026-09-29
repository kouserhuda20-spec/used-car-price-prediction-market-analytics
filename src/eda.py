import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from preprocess import load_data, clean_data

OUT=Path("reports/figures")
OUT.mkdir(parents=True, exist_ok=True)

df=clean_data(load_data())
print(df.describe(include="all"))
print("\nMissing values:\n", df.isna().sum())

for col in ["brand","fuel","transmission","location"]:
    ax=df.groupby(col)["price_lakh"].mean().sort_values(ascending=False).plot(kind="bar", figsize=(9,5), title=f"Average Price by {col.title()}")
    ax.set_ylabel("Price (₹ lakh)")
    plt.tight_layout()
    plt.savefig(OUT/f"avg_price_by_{col}.png", dpi=160)
    plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["kilometers"], df["price_lakh"], alpha=.35)
plt.xlabel("Kilometers"); plt.ylabel("Price (₹ lakh)"); plt.title("Price vs Mileage")
plt.tight_layout(); plt.savefig(OUT/"price_vs_mileage.png", dpi=160); plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["age"], df["price_lakh"], alpha=.35)
plt.xlabel("Vehicle Age"); plt.ylabel("Price (₹ lakh)"); plt.title("Price vs Vehicle Age")
plt.tight_layout(); plt.savefig(OUT/"price_vs_age.png", dpi=160); plt.close()

print("\nTop brands by average price:")
print(df.groupby("brand")["price_lakh"].mean().sort_values(ascending=False).round(2))
