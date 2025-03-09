import os
import pandas as pd

# Define the folder containing the CSV files
folder_path = "../../../Desktop/prepositions"
output_file = "combined_output.csv"

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Initialize an empty list to store DataFrames
dataframes = []

# Read each CSV and append it to the list
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv(os.path.join(folder_path, output_file), index=False)

print(f"Combined CSV saved as {output_file} in {folder_path}")