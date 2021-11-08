import requests
import pandas as pd

class Dexlab:
    def __init__(self):
        self.base = "https://api.dexlab.space"
        self.pairs_infos = None

    def get_pairs(self):
        endpoint = "/v1/pairs"
        data = self.make_request(endpoint, "GET")
        df = pd.DataFrame(data)
        self.pairs_infos = df
        return df

    def get_orderbook(self, address):
        endpoint = "/v1/orderbooks/" + address
        data = self.make_request(endpoint, "GET")
        return data

    def get_market_price(self, address):
        endpoint = f"/v1/prices/{address}/last"
        data = self.make_request(endpoint, "GET")
        return data


    def make_request(self, endpoint, method):
        endpoint = endpoint
        url = self.base + endpoint

        if method == "GET":
            r = requests.get(url)
            if r.status_code == 200:
                r = r.json()
                if "data" in r.keys():
                    datas = r["data"]
                    return datas
                else:
                    print(f"Cannot get data for this endpoint: {endpoint}")
                    return None
            else:
                print(f"Error {r.status_code} with {method} for {endpoint}")