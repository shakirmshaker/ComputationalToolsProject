# Crawling

We provide an option to run the crawling anonymously by using **Tor**.

We leverage [asyncio](https://docs.python.org/3/library/asyncio.html) library for our requests and utilize [beautifulsoup](https://pypi.org/project/beautifulsoup4) to get the information we need.

## Usage

The following is the crawling usage.

```bash
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
    Crawling Copenhagen addresses:
    python main.py -a Copenhagen

    Crawling property information:
    python main.py -d /path/to/addresses.json

    Merging JSON files:
    python main.py -o merged.json -i file1_properties.json file2_properties.json file3_properties.json

    Processing a JSON file:
    python main.py -p file_properties.json
```

To enable or disable TOR, modify the [**anonymity**](/src/scraping/main.py) variable (by default set to ```False```):
```python
bo_crawler = PropertyCrawler(root_url=root_url, input_file=args.datafile, anonymity=True)
```

### [TorHandler](/src/scraping/torhandler.py)

The crawling method using **Tor** was inspired by [Tor IP rotation](https://github.com/baatout/tor-ip-rotation-python-example). I conducted the crawling at a Fedora 37 Linux machine.
You can find the requirements for Linux in [PyTorStemPrivoxy](https://github.com/FrackingAnalysis/PyTorStemPrivoxy).

## .env

The following variables can be found at ```.template.env```.
```bash
RENT_URL=   # The property website (https://www.boligsiden.dk/)
API_URL=    # The Danish Address API (https://dawadocs.dataforsyningen.dk/dok/api#adresser-1)    
TOR_PWD=    # Your Tor password if you use anonymous crawling
PAGE_SIZE=  # The page size when collecting addresses from Danish Address API 
```

## Files

```bash
.
|-- README.md                   # General information on the crawling and running instructions
|-- danishaddresscrawler.py     # Class for collecting addresses per municipality
|-- jsonmerger.py               # Json merger in case the results of crawling are on different files
|-- jsonprocessor.py            # Converting .json files to .csv while filtering columns for processing
|-- main.py                     # Main function with usage
|-- propertycrawler.py          # Class for crawling asynchronously (+ option for anonymous crawling) 
`-- torhandler.py               # Custom Tor handler for http requests to use for anonymous crawling
```
