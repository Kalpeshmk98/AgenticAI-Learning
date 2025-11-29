import os
import pandas as pd

print("STARTING po_summary.py")
print("Current working dir:", os.getcwd())
print("Listing files in current folder:")
for f in os.listdir("."):
    print("  ", f)

data_path = os.path.join("datasets", "purchase_orders.csv")
print("Looking for dataset at:", data_path)
print("Exists?", os.path.exists(data_path))

# ------------------------------------------------------
# LOAD DATASET SAFELY
# ------------------------------------------------------
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    print("Loaded dataset. Rows:", len(df))

    # Convert numeric columns
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)

    # Compute line_total
    df["line_total"] = df["quantity"] * df["unit_price"]

    # Summary stats
    total_spend = df["line_total"].sum()
    top_vendors = (
        df.groupby("vendor_name")["line_total"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print("\nTotal Spend:", total_spend)
    print("\nTop 5 Vendors by Spend:")
    print(top_vendors)

else:
    print("Dataset NOT found. Please place purchase_orders.csv in datasets/")

print("SCRIPT END")