import pandas as pd
from pathlib import Path
import re

# --- Folder path ---
data_folder = Path(r"C:\Users\auguc\OneDrive\Documents\GitHub\mse-api-assignment-main\mse-api-assignment-main\data\csv_files")

# --- Collect all file types ---
all_files = list(data_folder.glob("*.txt")) + list(data_folder.glob("*.csv")) + list(data_folder.glob("*.xls"))
df_list = []

print(f"📁 Found {len(all_files)} files to process...\n")

def parse_txt_file(file_path):
    """Extract structured table from MSE text reports."""
    print(f"🔍 Parsing TXT file: {file_path.name}")

    rows = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Find where the table starts
    start_idx = None
    for i, line in enumerate(lines):
        if re.search(r'(?i)(company|ticker|symbol)', line):
            start_idx = i
            break

    if start_idx is None:
        print(f"⚠️ No header line found in {file_path.name}, skipping.")
        return pd.DataFrame()

    header_line = lines[start_idx].strip()
    headers = re.split(r'\s{2,}', header_line.lower().strip())
    print(f"🧾 Detected headers: {headers}")

    # Parse subsequent lines until a footer or blank line
    for line in lines[start_idx + 1:]:
        line = line.strip()
        if not line or "page" in line.lower() or "summary" in line.lower():
            break

        cols = re.split(r'\s{2,}', line)
        if len(cols) >= len(headers):
            rows.append(cols[:len(headers)])

    if not rows:
        print(f"❌ No data rows found in {file_path.name}.")
        return pd.DataFrame()

    df = pd.DataFrame(rows, columns=headers)
    return df


# --- MAIN LOOP ---
for file in all_files:
    print(f"\n📂 Processing file: {file.name}")

    # Load according to extension
    if file.suffix == ".txt":
        df = parse_txt_file(file)
    elif file.suffix == ".csv":
        df = pd.read_csv(file, dtype=str, on_bad_lines='skip', low_memory=False)
    elif file.suffix == ".xls":
        df = pd.read_excel(file, dtype=str)
    else:
        continue

    if df.empty:
        print(f"⚠️ Skipping empty or invalid file: {file.name}")
        continue

    # --- CLEAN & STANDARDIZE ---
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Try to detect ticker/date columns
    possible_ticker_names = ['ticker', 'symbol', 'code', 'company']
    possible_date_names = ['date', 'tradedate', 'trading_date']

    ticker_col = next((c for c in df.columns if any(k in c for k in possible_ticker_names)), None)
    date_col = next((c for c in df.columns if any(k in c for k in possible_date_names)), None)

    if not ticker_col or not date_col:
        print(f"❌ No useful columns found in {file.name}, skipping.")
        continue

    df = df.dropna(subset=[ticker_col, date_col])

    # Keep only useful columns
    useful_cols = [c for c in df.columns if any(x in c for x in [
        'ticker', 'symbol', 'code', 'company', 'date', 'open', 'high', 'low', 'close', 'volume', 'trades'
    ])]

    df = df[useful_cols]

    df_list.append(df)
    print(f"✅ Extracted {len(df)} rows from {file.name}")


# --- MERGE ALL ---
if not df_list:
    raise ValueError("No valid tabular data found in provided files.")

merged_df = pd.concat(df_list, ignore_index=True)
merged_df = merged_df.drop_duplicates().dropna(how="all")

# --- SAVE ---
output_file = data_folder / "merged.csv"
merged_df.to_csv(output_file, index=False)

print("\n✅ Clean merged file saved:", output_file)
print("🧾 Columns in merged file:", list(merged_df.columns))
print(merged_df.head(10))
