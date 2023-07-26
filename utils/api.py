import json

from utils.http_methods import HttpMethods

"""Методы для тестирования Google Maps API"""

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = {"?key": "qaclick123"}  # Параметр для всех запросов


class GoogleMapsApi:

    @staticmethod
    def create_new_place():
        """Метод для создания новой локации"""
        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Front house",
            "phone_number": "(+91) 983 893 3937",
            "address": f'street',
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'  # ресурс метода POST
        post_url = base_url + post_resource
        print(post_url)
        response_post = HttpMethods.post(url=post_url, body=json_for_create_new_place)
        print(response_post.text)
        return response_post
















