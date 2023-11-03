"""
This class is used for crawling information from rental website
"""

import json
import random
import time
import requests
import os
import urllib.error.HTTPError

from bs4 import BeautifulSoup

from torhandler import TorHandler


class PropertyCrawler():

    def __init__(self, root_url: str, input_file: str, anonymity=True) -> None:
        self.root_url = root_url
        if anonymity:
            self.tor_handler = TorHandler()
        self.municipality = None
        self.addresses_list = self.__get_addresses(input_file)
        self.anonymity = anonymity

    def __get_addresses(self, input_file: str) -> list:
        try:
            with open(input_file, mode="r") as sf:
                json_data_list = json.load(sf)

            addresses_list = []
            for json_data in json_data_list:
                addresses_list.append(self.root_url + json_data["slugified_adresse"]
                                      + "-" + json_data["kvhx"])
                if self.municipality == None:
                    self.municipality = json_data["municipality"]

        except FileNotFoundError:
            print("Error: {} does not exist".format(input_file))

        return addresses_list

    def crawl(self) -> None:
        if self.anonymity:
            self.__tor_crawl()
        else:
            self.__async_crawl()

    def __tor_crawl(self) -> None:
        ip = self.tor_handler.open_url("http://icanhazip.com/")
        print("Log: First IP: {}".format(ip))
        destination_file = str(self.municipality) + "_properties.json"

        if not os.path.isfile(destination_file):
            with open(destination_file, mode="w") as df:
                df.write(json.dumps([], indent=2))

        for address in self.addresses_list:

            with open(file=destination_file, mode="r") as sf:
                source_file = json.load(sf)

            # If address exists in json file, do not crawl

            if any(address.endswith(address_["props"]["pageProps"]["dataLayer"]["virtualPagePath"]) for address_ in source_file):
                print("Log: \nAddress already exists in file\n")
                continue

            print("Log: Address to crawl: {}".format(address))
            # Random sleep time to not overload the site and be less sus
            time.sleep(random.randint(1, 3))
            self.tor_handler.renew_connection()
            ip = self.tor_handler.open_url("http://icanhazip.com/")
            print("Log: Current IP: {}".format(ip))

            # Add exception for specific error in the handler 
            try:
                content = self.tor_handler.open_url(address)
            except urllib.error.HTTPError:
                # This one failed, ignore for now, for some reason the TOR handler crushed
                # It will be recrawled anyway
                print("Error: Tor handler crushed.")
                continue

            soup = BeautifulSoup(content)
            json_data = json.loads(soup.find("script", type="application/json").text)
            print("Log: Json data: {}".format(json_data))

            source_file.append(json_data)
            with open(file=destination_file, mode="w") as df:
                df.write(json.dumps(source_file, indent=2))

    def __async_crawl(self) -> None:
        all_data = []

        for address in self.addresses_list:
            print("Address to crawl: {}".format(
                'https://www.boligsiden.dk/adresse/' + address))
            # Random sleep time to not overload the site and be less sus
            time.sleep(random.randint(1, 3))
            response = requests.get(
                'https://www.boligsiden.dk/adresse/' + address)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
                if script_tag:
                    json_text = script_tag.string
                    data = json.loads(json_text)
                    all_data.append(data)
                    # print("Json data: {}".format(data))
                    print("Dataset added successfully!")
                else:
                    print(f"Script tag not found for {address}")
            else:
                print(f"Failed to retrieve {address}")

        with open('XXX_addresses_data.json', 'w') as f:
            json.dump(all_data, f, indent=4)
