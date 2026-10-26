from pathlib import Path
import pandas as pd

# Locate the project directory
project_dir = Path(__file__).resolve().parent.parent

# Load the cleaned traffic data
file_path = project_dir / "cleaned_Charlotte_traffic.csv"
df = pd.read_csv(file_path)

# Display sample traffic records
print("Charlotte Traffic Prediction Demo")
print(df.head())

# Display congestion distribution
if "traffic_level" in df.columns:
    print(df["traffic_level"].value_counts())
