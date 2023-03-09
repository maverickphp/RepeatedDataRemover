import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('input.csv')

# Loop through each column in the dataframe
for column in df.columns:
    # Check if the column contains string or numeric data
    if df[column].dtype == 'object':
        # Strip leading and trailing spaces from string data
        df[column] = df[column].str.strip()
    else:
        # For numeric data, convert to string and strip leading and trailing spaces
        df[column] = df[column].astype(str).str.strip()

    # Remove duplicates from the column
    df[column] = df[column].drop_duplicates()

# Write the cleaned dataframe to a new CSV file
df.to_csv('output.csv', index=False)
