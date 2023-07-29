import allure
import requests
from utils.logger import Logger


class HttpMethods:
    """Список HTTP методов"""

    @staticmethod
    def get(url):
        with allure.step(f"GET request to URL '{url}'"):
            Logger.add_requests(url, method="GET")
            response = requests.get(url, headers={}, cookies={})
            Logger.add_response(response)
            return response

    @staticmethod
    def post(url, body):
        with allure.step(f"POST request to URL '{url}'"):
            Logger.add_requests(url, method="POST")
            response = requests.post(url, json=body, headers={}, cookies={})
            Logger.add_response(response)
            return response

    @staticmethod
    def put(url, body):
        with allure.step(f"PUT request to URL '{url}'"):
            Logger.add_requests(url, method="PUT")
            response = requests.put(url, json=body, headers={}, cookies={})
            Logger.add_response(response)
            return response

    @staticmethod
    def delete(url, body):
        with allure.step(f"DELETE request to URL '{url}'"):
            Logger.add_requests(url, method="DELETE")
            response = requests.delete(url, json=body, headers={}, cookies={})
            Logger.add_response(response)
            return response
