import json
from flatten_json import flatten
import pandas as pd

class JSONProcessor:
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.json_data = None
        self.flattened_data = None
        self.output_path = json_file.split(".")[0]  

    def call(self):
        with open(self.json_file, 'r') as file:
            self.json_data = json.load(file)
        self.flatten()
        self.convert()

    def convert(self) -> None:
        try:
            df = pd.json_normalize(self.flattened_data)
            csv_file = self.output_path + ".csv"
            df.to_csv(csv_file, index=False)
            print(f"Log: Converted file {self.json_file} into csv {csv_file}")
        except Exception as e:
            print(f"Error: Could not convert to CSV. [{e}]")

    def flatten(self) -> None:
        try:
            self.flattened_data = [flatten(d) for d in self.json_data]
        except Exception as e:
            print(f"Error: Could not flatten JSON. [{e}]")
