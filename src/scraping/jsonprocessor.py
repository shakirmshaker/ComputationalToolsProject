import os
import json
from flatten_json import flatten
import pandas as pd
from tqdm import tqdm


class JSONProcessor:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.json_data = None
        self.flattened_data = None
        self.output_dir = os.path.dirname(json_file)
        self.output_filename = os.path.splitext(os.path.basename(json_file))[0]
        self.output_path = os.path.join(self.output_dir, self.output_filename)
        self.csv_filename = self.output_path + ".csv"

    def call(self):
        with open(self.json_file, "r") as file:
            self.json_data = json.load(file)
        self.flatten()
        self.append_to_csv()

    def flatten(self) -> None:
        try:
            self.flattened_data = [flatten(d) for d in self.json_data]
        except Exception as e:
            print(f"Error: Could not flatten JSON. [{e}]")

    def append_to_csv(self) -> None:
        try:
            is_header_written = not os.path.exists(self.csv_filename)
            for item in tqdm(self.flattened_data, desc=f"Processing {self.json_file}"):
                df = pd.DataFrame([item])
                df.to_csv(self.csv_filename, mode='a',
                          index=False, header=is_header_written)
                is_header_written = True
            print(f"Log: Appended data to {self.csv_filename}.")
        except Exception as e:
            print(f"Error: Could not append to CSV. [{e}]")

    def save_flattened_json(self) -> None:
        with open(self.output_path + "_flattened.json", "w") as f:
            json.dump(self.flattened_data, f, indent=4)
