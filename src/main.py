import os
import argparse
from dotenv import load_dotenv

from propertycrawler import PropertyCrawler
from danishaddresscrawler import DanishAddressCrawler
from jsonmerger import JSONMerger
from jsonprocessor import JSONProcessor


def argument_help():
    help_text = """
    Usage: script.py [-h] [-a ADDRESS] [-d DATAFILE] [-o OUTPUT] [-i INPUT [INPUT ...]] [-p PROCESS]

    This script can crawl Danish addresses, crawl property information, merge JSON files, or process a single JSON file.

    Address Crawler Arguments:
    -a, --address      Specify a municipality for Danish address crawler. 
                       This option triggers the Danish Address Crawler.

    Property Crawler Arguments:
    -d, --datafile     Specify the input file name for the property crawler. 
                       This option triggers the Property Crawler.

    JSON Merger/Processor Arguments:
    -o, --output       Specify the output JSON file for merging or processing.
                       This is a required argument for JSON merging or processing.
    -i, --input        List of input JSON files to merge. Separate multiple files with spaces.
                       This option, used with -o, triggers the JSON Merger.
    -p, --process      Specify a single JSON file to post-process.
                       This option, used with -o, triggers the JSON Processor.

    General Arguments:
    -h, --help         Show this help message and exit.

    Examples:
    Crawling Danish addresses:
    python main.py -a Copenhagen

    Crawling property information:
    python main.py -d x_addresses.json

    Merging JSON files:
    python main.py -o merged.json -i file1_properties.json file2_properties.json file3_properties.json

    Processing a JSON file:
    python main.py -o processed.json -p file_properties.json
    """
    print(help_text)

def main():
    load_dotenv()
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive"
    }
    parser = argparse.ArgumentParser(description="A multifunctional script for crawling, merging, and processing data.")
    parser.add_argument("-a", "--address", help="Specify a municipality for Danish address crawler.")
    parser.add_argument("-d", "--datafile", help="Specify the input file name for property crawler.")
    parser.add_argument("-o", "--output", help="The output JSON file")
    parser.add_argument("-i", "--input", nargs="+", help="The input JSON files to merge")
    parser.add_argument("-p", "--process", help="The file to post-process")
    
    args = parser.parse_args()

    if args.address:
        root_url = os.getenv("API_URL")
        page_number = os.getenv("PAGE_SIZE")
        da_crawler = DanishAddressCrawler(page_number, root_url, headers, municipality=args.address)
        da_crawler.crawl()
    elif args.datafile:
        root_url = os.getenv("RENT_URL")
        bo_crawler = PropertyCrawler(root_url=root_url, input_file=args.datafile, anonymity=True)
        bo_crawler.crawl()
    elif args.input and args.output:
        json_merger = JSONMerger(args.input, args.output)
        json_merger.call()
    elif args.process and args.output:
        json_process = JSONProcessor(args.process)
        json_process.call()
    elif args.help:
        argument_help()
    else:
        argument_help()
        exit(1)

if __name__ == "__main__":
    main()