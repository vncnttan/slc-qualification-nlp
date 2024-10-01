import pandas as pd

# Load the dataset into a DataFrame
file_path = "Case 1\lyric-dataset\lyrics-data.csv"  # Replace with the actual file path
df = pd.read_csv(file_path)

# Filter the DataFrame based on the language column
df_filtered = df[df['language'] == 'en']  # Replace 'language' with the actual column name
df_filtered = df_filtered.head(500)

# Save the filtered DataFrame to a new CSV file
output_file_path = "Case 1\lyric-dataset\en-lyrics-data.csv"  # Replace with the desired output file path
df_filtered.to_csv(output_file_path, index=False)
