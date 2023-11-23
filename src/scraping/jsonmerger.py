import json
import os

class JSONMerger:

    def __init__(self, json_list: list, output_path: str) -> None:
        self.json_list = json_list
        self.output_path = output_path
        self.json_merged = []
    
    def call(self) -> None:
        if self.merge():
            self.save()
        print("Log: Merged and saved file ...")

    def merge(self) -> bool:
        try:
            for json_file in self.json_list:
                if not os.path.exists(json_file):
                    print(f"Error: File {json_file} does not exist.")
                    return False
                with open(json_file, "r") as file:
                    data = json.load(file)                    
                    self.json_merged.extend(data)
            return True
        except Exception as e:
            print(f"Error: An exception occurred. [{e}]")
            return False

    def save(self) -> None:
        try:
            with open(self.output_path + ".json", "w") as file:
                json.dump(self.json_merged, file, indent=4)
        except Exception as e:
            print(f"Error: Could not save file. [{e}]")
