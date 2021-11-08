import requests
import pandas as pd

class Dexlab:
    def __init__(self):
        self.base = "https://api.dexlab.space"
        self.pairs_infos = None

    def get_pairs(self):
        endpoint = "/v1/pairs"
        data = self._make_request(endpoint, "GET")
        return data

    def get_orderbook(self, address):
        endpoint = "/v1/orderbooks/" + address
        data = self._make_request(endpoint, "GET")
        return data

    def get_market_price_by_address(self, address):
        endpoint = f"/v1/prices/{address}/last"
        data = self._make_request(endpoint, "GET")
        return data

    def get_market_prices(self):
        endpoint = "/v1/prices"
        data = self._make_request(endpoint, "GET")
        return data

    def get_market_price_recent(self):
        endpoint = "/v1/prices/recent"
        data = self._make_request(endpoint, "GET")
        return data

    def get_24h_ago_price(self, address):
        endpoint = f"/v1/prices/{address}/closing-price"
        data = self._make_request(endpoint, "GET")
        return data

    def get_volumes(self):
        endpoint = "/v1/volumes"
        data = self._make_request(endpoint, "GET")
        return data

    def get_volume_by_address(self, address):
        endpoint = f"/v1/volumes/{address}"
        data = self._make_request(endpoint, "GET")
        return data

    def get_latests_trades(self):
        endpoint = "/v1/trades"
        data = self._make_request(endpoint, "GET")
        return data

    def get_trades_by_address(self, address):
        endpoint = f"v1/trades/{address}/24h"
        data = self._make_request(endpoint, "GET")
        return data

    def get_latest_trade_24h(self, address):
        endpoint = f"v1/trades/{address}/last"
        data = self._make_request(endpoint, "GET")
        return data


######## HELPERS #########

    def _make_request(self, endpoint, method):
        endpoint = endpoint
        url = self.base + endpoint

        if method == "GET":
            r = requests.get(url)
            if r.status_code == 200:
                r = r.json()
                if "data" in r.keys():
                    data = r["data"]
                    return data
                else:
                    print(f"Cannot get data for this endpoint: {endpoint}")
                    return None
            else:
                print(f"Error {r.status_code} with {method} for {endpoint}")
                return None