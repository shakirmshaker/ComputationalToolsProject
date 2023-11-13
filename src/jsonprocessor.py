import os
import json
from flatten_json import flatten
import pandas as pd

class JSONProcessor:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.json_data = None
        self.flattened_data = None
        self.output_dir = os.path.dirname(json_file)
        self.output_filename = os.path.splitext(os.path.basename(json_file))[0]
        self.output_path = os.path.join(self.output_dir, self.output_filename)

    def call(self):
        with open(self.json_file, "r") as file:
            self.json_data = json.load(file)
        self.flatten()
        self.convert()

    def flatten(self) -> None:
        try:
            self.flattened_data = [flatten(d) for d in self.json_data]
        except Exception as e:
            print(f"Error: Could not flatten JSON. [{e}]")

    def convert(self) -> None:
        try:
            df = pd.json_normalize(self.flattened_data)
            csv_file = self.output_path + ".csv"
            df.to_csv(csv_file, index=False)
            print(f"Log: Converted file {self.json_file} into csv {csv_file}.")
        except Exception as e:
            print(f"Error: Could not convert to CSV. [{e}]")

    def save(self) -> None:
        with open(self.output_path + "_flattened.json", "w") as f:
            json.dump(self.flattened_data, f, indent=4)
