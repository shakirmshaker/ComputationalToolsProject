import argparse
from jsonmerger import JSONMerger

def main():
    parser = argparse.ArgumentParser(description="Merge multiple JSON files into one.")
    parser.add_argument("-o", "--output", required=True, help="The output JSON file")
    parser.add_argument("-i", "--input", nargs="+", required=True, help="The input JSON files to merge")

    args = parser.parse_args()
    json_merger = JSONMerger(args.input, args.output)

    json_merger.call()
    json_merger.convert()

if __name__ == "__main__":
    # Example:
    # python main_postprocessing.py -o merged -i ../data/147a_addresses_data.json ../data/147b_addresses_data.json ../data/147c_addresses_data.json ../data/147c_addresses_data.json ../data/147d_addresses_data.json ../data/147e_addresses_data.json ../data/147h_addresses_data.json 
    main()