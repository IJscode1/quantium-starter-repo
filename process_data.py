import pandas as pd
import glob

files = glob.glob("data/*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
df = df[df["product"] == "pink morsel"]
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
df["sales"] = df["quantity"] * df["price"]
df = df[["sales", "date", "region"]]
df = df.sort_values("date")
df.to_csv("formatted_output.csv", index=False)
print(f"Done. {len(df)} rows written to formatted_output.csv")