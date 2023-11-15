import pandas as pd
import json
import os
import re
from tqdm import tqdm
from collections import defaultdict

def flatten_json(y):
    """ Flatten nested JSON and return flat DataFrame. """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def append_df_to_csv(df, filename, mode='a', header=False):
    """ Append DataFrame to CSV with option to include header. """
    df.to_csv(filename, mode=mode, header=header, index=False)

def get_file_groups(directory):
    """ Group files by the 'XXX' prefix in the filename. """
    file_groups = defaultdict(list)
    pattern = re.compile(r"(\d{3})([a-z]?_addresses_data)\.json")

    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            file_groups[prefix].append(filename)
    
    return file_groups

# Directory containing the JSON files
directory = '.'

# Get file groups
file_groups = get_file_groups(directory)

# Process each file group
for prefix, files in file_groups.items():
    # Initialize CSV file with header for each group
    is_header_written = False
    csv_filename = f"{prefix}_data.csv"

    for file_name in files:
        with open(os.path.join(directory, file_name), 'r') as file:
            data = json.load(file)
            for item in tqdm(data, desc=f"Processing {file_name}"):
                flattened_data = flatten_json(item)
                df = pd.DataFrame([flattened_data])
                append_df_to_csv(df, csv_filename, header=not is_header_written)
                is_header_written = True  # Set to True after the first write operation

    print(f"Data extraction complete for group {prefix}. CSV file '{csv_filename}' saved.")

print("All processing complete.")