# Path: uc-0c/app.py

import pandas as pd
import argparse


# -------------------------------
# Load data
# -------------------------------
def load_budget_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise Exception(f"❌ Failed to load file: {e}")


# -------------------------------
# Compute growth safely
# -------------------------------
def compute_growth(prev, curr):
    # Handle nulls
    if pd.isna(prev) or pd.isna(curr):
        return None

    # Avoid division by zero
    if prev == 0:
        return None

    # Growth calculation (allow negative)
    return ((curr - prev) / prev) * 100


# -------------------------------
# Apply growth calculation
# -------------------------------
def apply_growth(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        raise ValueError("❌ Not enough numeric columns for growth calculation")

    # Take last two numeric columns
    prev_col = numeric_cols[-2]
    curr_col = numeric_cols[-1]

    df["growth_percent"] = df.apply(
        lambda row: compute_growth(row[prev_col], row[curr_col]),
        axis=1
    )

    # ✅ FINAL POLISH: round values
    df["growth_percent"] = df["growth_percent"].round(2)

    return df


# -------------------------------
# Save output
# -------------------------------
def save_output(df, output_path):
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        raise Exception(f"❌ Failed to save file: {e}")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    try:
        df = load_budget_data(args.input)
        df = apply_growth(df)
        save_output(df, args.output)

        print("✅ UC-0C completed successfully")

    except Exception as e:
        print("❌ Error:", str(e))