"""
This class is used for crawling information from rental website
"""

import json
import random
import time
import requests

from bs4 import BeautifulSoup

from torhandler import TorHandler


class PropertyCrawler():

	def __init__(self, root_url, input_file, anonymity=True):
		self.root_url = root_url
		self.addresses_list = self.__get_addresses(input_file)
		if anonymity:
			self.tor_handler = TorHandler()
		self.anonymity = anonymity
		

	def __get_addresses(self, input_file : str) -> list:
		try:
			with open(input_file, mode="r") as sf:
				json_data_list = json.load(sf)
			
			addresses_list = []
			for json_data in json_data_list:
				addresses_list.append(self.root_url + json_data["slugified_adresse"] \
					+ "-" + json_data["kvhx"])

		except FileNotFoundError:
			print("Error: {} does not exist".format(input_file))

		return addresses_list
	
	def crawl(self):
		if self.anonymity:
			self.__tor_crawl()
		else:
			self.__async_crawl()
	
	def __tor_crawl(self):
		ip = self.tor_handler.open_url("http://icanhazip.com/")
		print("First IP: {}".format(ip))
		for address in self.addresses_list:
			print("Address to crawl: {}".format(address))
			# Random sleep time to not overload the site and be less sus
			time.sleep(random.randint(1, 3))
			self.tor_handler.renew_connection()
			ip = self.tor_handler.open_url("http://icanhazip.com/")
			print("Current IP: {}".format(ip))
			content = self.tor_handler.open_url(address)
			soup = BeautifulSoup(content)
			json_data = json.loads(soup.find("script", type="application/json").text)
			print("Json data: {}".format(json_data))

			formatted_data = json.dumps(json_data, indent=4)
			print("Formatted json:\n{}".format(formatted_data))

	def __async_crawl(self):
		# TODO: Simple crawler
		# Care to not overload the site, also put proper agent to not get blocked.
		# Follow the same approach as the `danishaddresscrawler` file.
		all_data = []

		for address in self.addresses_list:
			print("Address to crawl: {}".format('https://www.boligsiden.dk/adresse/' + address))
			# Random sleep time to not overload the site and be less sus
			time.sleep(random.randint(1, 3))
			response = requests.get('https://www.boligsiden.dk/adresse/' + address)
			if response.status_code == 200:
				soup = BeautifulSoup(response.content, 'html.parser')
				script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
				if script_tag:
					json_text = script_tag.string
					data = json.loads(json_text)
					all_data.append(data)
					#print("Json data: {}".format(data))
					print("Dataset added successfully!")
				else:
					print(f"Script tag not found for {address}")
			else:
				print(f"Failed to retrieve {address}")

		with open('XXX_addresses_data.json', 'w') as f:
			json.dump(all_data, f, indent=4)
		#raise NotImplementedError