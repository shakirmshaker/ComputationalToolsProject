"""
Class used for crawling addresses by municipality using https://api.dataforsyningen.dk/adresser
"""
import asyncio
import json
from slugify import slugify

import aiohttp


class DanishAddressCrawler():

    def __init__(self, page_number, root_url, headers, municipality="Copenhagen") -> None:
        self.page_number = page_number
        self.root_url = root_url
        self.headers = headers
        self.municipality = self.__get_municipality_records()[municipality]

    def __get_municipality_records(self) -> dict:
        return {
            "Copenhagen": 101,
            "Frederiksberg": 147,
            "Gentofte": 157,
            "Gladsaxe": 159,
            "Helsingør": 217,
            "Rudersdal": 230,
            "Lyngby-Taarbæk": 173,
            "Hvidovre": 167,
            "Hillerød": 219,
            "Høje-Taastrup": 169,
            "Ballerup": 151,
            "Frederikssund": 250,
            "Egedal": 240,
            "Bornholm": 400,
            "Tårnby": 185,
            "Gribskov": 270,
            "Fredensborg": 210,
            "Furesø": 190,
            "Rødovre": 175,
            "Brøndby": 153,
            "Halsnæs": 260,
            "Albertslund": 165,
            "Herlev": 163,
            "Hørsholm": 223,
            "Allerød": 201,
            "Glostrup": 161,
            "Ishøj": 183,
            "Vallensbæk": 187,
            "Dragør": 155,
        }

    @staticmethod
    def is_valid(response: dict) -> bool:
        return not "type" in response
    
    def crawl(self):
        asyncio.run(self.__get_results())

    async def __get_results(self) -> None:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            
            tasks = []
            # TODO: Fix range, add custom range. Is there a way to get number of records?
            for page in range(0, 1000):
                tasks.append(asyncio.ensure_future(self.__get_results_page(page, session)))

            json_data_list = await asyncio.gather(*tasks)
            json_data_flattened_list = [item for sublist in json_data_list if isinstance(sublist, list) for item in sublist]

            json_data_file = []
            for json_data in json_data_flattened_list:
                if DanishAddressCrawler.is_valid(json_data):
                    kvhx = json_data["kvhx"]
                    adressebetegnelse = json_data["adressebetegnelse"]
                    id = json_data["id"]
                    slugified_adresse = slugify(adressebetegnelse)
                    json_data_file.append({
                        "id" : id,
                        "kvhx" : kvhx,
                        "adressebetegnelse" : adressebetegnelse,
                        "slugified_adresse" : slugified_adresse,
                        "municipality": self.municipality
                    })
                    print("========================")
                    print("`kvhx`: {}".format(kvhx))
                    print("`id`: {}".format(id))
                    print("`adressebetegnelse`: {}".format(adressebetegnelse))
                    print("`slugified_adresse`: {}".format(slugified_adresse))
            
            with open(str(self.municipality) + "_addresses.json", mode="w", encoding="utf-8") as df:
                json.dump(json_data_file, df)

    async def __get_results_page(self, page, session, retries=5):
        url = self.root_url + "?per_side=" + str(self.page_number) \
            + "&side=" + str(page) + "&kommunekode=" + str(self.municipality)
        async with session.get(url) as response:
            json_data = await response.json()
            status = response.status
            print("Response status: {}".format(status))
            if response.status == 400 and retries > 0:
                await asyncio.sleep(1)
                json_data = await self.__get_results_page(page, session, retries - 1)
            return json_data
