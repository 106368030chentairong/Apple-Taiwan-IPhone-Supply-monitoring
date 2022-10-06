import requests
import time
import json

class iphone_check_api:
    def __init__(self) -> None:
        self.headers = {}

    def requests_url(self, ask_typ, url):
        try:
            response = requests.request(ask_typ, url, headers=self.headers)
        except requests.exceptions.Timeout:
            print("Timeout")
        except requests.exceptions.TooManyRedirects:
            print("Too Many Redirects")
        except requests.exceptions.RequestException as e:
            print(e)
        return response
    
    def get_partNumber(self, iphone_name):
        # iphone_name relu is "iphone14pro" or "iphone14"
        url = "https://www.apple.com/tw/shop/product-locator-meta?family=" + iphone_name
        response = self.requests_url("GET",url)

        product_number_list = []
        try:
            json_data = json.loads(response.text)
            body_data = json_data["body"]

            for product in body_data["productLocatorOverlayData"]["productLocatorMeta"]["products"] :
                product_number_list.append([product["productTitle"], product["partNumber"]])

            return product_number_list
        except KeyError:
            return None
        except Exception:
            return None
    
    def check_store_state(self, partNumber):
        url = "https://www.apple.com/tw/shop/pickup-message-recommendations?mts.0=regular&location=110&product=" + partNumber
        response = self.requests_url("GET",url)

        store_list = []
        try:
            json_data = json.loads(response.text)
            body_data = json_data["body"]
            stores_msg = body_data["PickupMessage"]["stores"]

            for store in stores_msg:
                pickup_list = []
                if store["partsAvailability"] != {}:
                    items = store["partsAvailability"].items()
                    for Key, value in items:
                        pickup_list.append([value["messageTypes"]["regular"]["storePickupProductTitle"], value["pickupSearchQuote"]])
                store_list.append([store["storeName"],pickup_list])
            return store_list
        except KeyError:
            return None
        except Exception:
            return None

        