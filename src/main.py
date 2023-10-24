import os

from dotenv import load_dotenv

from propertycrawler import PropertyCrawler
from danishaddresscrawler import DanishAddressCrawler


def main():
    load_dotenv()
    # TODO: Add arguments
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive"
    }

    option = input("Options:\n1. Crawl addresses by municipality\n2. Crawl addresses information\nChoose an option (1 or 2): ")

    if option == "1":
        # 1. Crawl addresses by municipality
        root_url = os.getenv("API_URL")
        page_number = os.getenv("PAGE_SIZE")
        input_municipality = input("Please provide a municipality (e.g. Copenhagen): ")
        da_crawler = DanishAddressCrawler(page_number, root_url, headers, municipality=input_municipality)
        da_crawler.crawl()
    elif option == "2":
        # 2. Crawl addresses information
        root_url =  os.getenv("RENT_URL")
        input_file = input("Please provide the input file name: ")
        bo_crawler = PropertyCrawler(root_url=root_url, input_file=input_file, anonymity= True)
        bo_crawler.crawl()
    else:
        print("Error: Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
