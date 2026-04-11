import pandas as pd
import glob

files = glob.glob("data/*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df.columns = df.columns.str.strip()
df["product"] = df["product"].astype(str).str.strip().str.lower()

df = df[df["product"].str.contains("pink", na=False)]

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .astype(float)
)

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["Sales"] = df["quantity"] * df["price"]

output_df = df[["Sales", "date", "region"]].copy()
output_df.columns = ["Sales", "Date", "Region"]

output_df.index += 1
output_df.to_csv("formatted_output.csv", index=False)

print(output_df.head())
print(f"Rows written: {len(output_df)}")