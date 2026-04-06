import pandas as pd
import argparse


# -------------------------------
# Detect correct text column
# -------------------------------
def get_text_column(df):
    possible_cols = ["complaint", "description", "text", "issue"]

    for col in possible_cols:
        if col in df.columns:
            return col

    raise ValueError("❌ No valid complaint column found in CSV")


# -------------------------------
# Classification with reason
# -------------------------------
def classify_complaint_with_reason(text):
    if not isinstance(text, str) or text.strip() == "":
        return "Other", "Empty or invalid input"

    text_lower = text.lower()

    billing_keywords = ["bill", "billing", "charge", "refund", "payment", "fee"]
    service_keywords = ["service", "support", "staff", "delay", "help"]
    network_keywords = ["network", "signal", "internet", "connect", "slow", "wifi"]

    for word in billing_keywords:
        if word in text_lower:
            return "Billing", f"Matched keyword: {word}"

    for word in service_keywords:
        if word in text_lower:
            return "Service", f"Matched keyword: {word}"

    for word in network_keywords:
        if word in text_lower:
            return "Network", f"Matched keyword: {word}"

    return "Other", "No matching keyword"


# -------------------------------
# Load data
# -------------------------------
def load_complaint_data(file_path):
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"❌ Error loading file: {e}")

    text_col = get_text_column(df)

    return df, text_col


# -------------------------------
# Apply classification
# -------------------------------
def apply_classification(df, text_col):
    df[["category", "reason"]] = df[text_col].apply(
        lambda x: pd.Series(classify_complaint_with_reason(x))
    )
    return df


# -------------------------------
# Save output
# -------------------------------
def save_output_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        raise Exception(f"❌ Error saving file: {e}")


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    try:
        df, text_col = load_complaint_data(args.input)
        df = apply_classification(df, text_col)
        save_output_data(df, args.output)

        print("✅ UC-0A completed successfully with reason column")

    except Exception as e:
        print("❌ Error:", str(e))