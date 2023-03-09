import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('input.csv')

# Loop through each column in the dataframe
for column in df.columns:
    # Check if the column contains string or numeric data
    if df[column].dtype == 'object':
        # Remove duplicates from string data
        df[column] = df[column].drop_duplicates()
    else:
        # Remove duplicates from numeric data
        df[column] = df[column].astype(str).drop_duplicates()

# Write the cleaned dataframe to a new CSV file
df.to_csv('output.csv', index=False)
