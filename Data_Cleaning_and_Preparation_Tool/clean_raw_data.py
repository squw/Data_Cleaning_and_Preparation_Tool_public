import pandas as pd
import numpy as np


def clean_df(df, columns_to_check, option="drop"): 
    """
    Clean a DataFrame by handling missing values and duplicates.

    Args:
        df (DataFrame): The DataFrame to be cleaned.
        columns_to_check (str or list): Column(s) to check for duplicates.
        option (str): The cleaning option. Default is "drop". 
                      Options: "drop" (drop rows with missing values), 
                               "replace" (replace missing values with "unknown").

    Returns:
        DataFrame: Cleaned DataFrame with missing values handled and duplicates removed.
    """

    # Placeholders for missing values
    placeholders = ["none", "unknown", "na", "missing", "n/a", "", "-", ".", "null", "nil", "not available"]

    # Replace placeholders with NaN
    df_nan = df.applymap(lambda x: np.nan if str(x).lower() in placeholders else x)

    if option == "replace":
        # Replace missing values with "unknown"
        df_nan = df_nan.fillna("unknown")
    elif option == "drop":
        # Drop rows with missing values
        df_nan = df_nan.dropna()
    else: 
        # Exit if option is invalid
        print("Invalid option input. Exiting program.")
        exit()

    # Remove duplicate rows based on specified columns
    df_nan.drop_duplicates(subset=columns_to_check, keep='first', inplace=True)

    # Reset index after cleaning
    df_nan = df_nan.reset_index(drop=True)
    
    return df_nan
    


# Define the CSV file path
csv_file_path = 'test_raw.csv'

df = pd.read_csv(csv_file_path)

print("\nOriginal DataFrame")
print(df)

columns_to_check = ["ID", "Name", "Gender"] # (df specific)

# Give option to drop the rows with missing values or replace it with "unknown"
option = "drop" # "replace" or "drop"


df = clean_df(df, columns_to_check, option)
print("\nDataFrame after cleaning: ")
print(df)