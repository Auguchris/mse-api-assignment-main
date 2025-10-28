import pandas as pd

# Path ya CSV
csv_path = r"C:\Users\auguc\OneDrive\Documents\GitHub\mse-api-assignment-main\mse-api-assignment-main\scripts\master.csv"

# Load CSV muri pandas
df = pd.read_csv(csv_path)

# Reba columns zose
print("Columns ziri muri CSV:")
print(df.columns.tolist())
