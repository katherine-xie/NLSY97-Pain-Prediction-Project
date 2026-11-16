
"""
Prepare the NLSY97 renamed dataset by renaming raw CSV columns.

"""

from pathlib import Path

import pandas as pd

from dsm_project.data.nlsy97_columns import COLUMN_NAMES

# ---------- Define File Paths ---------- 

# Find the project repository root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Original raw CSV
RAW_CSV = (
    PROJECT_ROOT
    / "data/local/nlsy97_raw_physical_activity_chronic_pain.csv"
)

# Output CSV with readable column names.
OUTPUT_CSV = (
    PROJECT_ROOT
    / "data/local/nlsy97_renamed_physical_activity_chronic_pain.csv"
)

# ---------- Prepare Dataset ---------- 

def main():

    # Load the raw dataset
    df = pd.read_csv(RAW_CSV, dtype=str, keep_default_na=False)

    # Check that the expected columns exist.
    missing = set(COLUMN_NAMES) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    # Rename columns using the mapping
    df = df.rename(columns=COLUMN_NAMES)

    # Save the renamed dataset as a new CSV
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"Saved {len(df):,} rows to {OUTPUT_CSV.name}")

# Guard
if __name__ == "__main__":
    main()
