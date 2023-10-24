"""
This controller can be used for anonymity in the crawling
"""

import os
from urllib.request import (ProxyHandler, Request, build_opener,
                            install_opener, urlopen)

from dotenv import load_dotenv
from stem import Signal
from stem.control import Controller


class TorHandler:
    def __init__(self):
        load_dotenv()
        self.password = os.getenv("TOR_PWD")
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"}

    def open_url(self, url):
        def _set_url_proxy():
            proxy_support = ProxyHandler({"http": "127.0.0.1:8118"})
            opener = build_opener(proxy_support)
            install_opener(opener)

        _set_url_proxy()
        request = Request(url, None, self.headers)
        return urlopen(request).read().decode("utf-8")

    def renew_connection(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=self.password)
            controller.signal(Signal.NEWNYM)
            controller.close()