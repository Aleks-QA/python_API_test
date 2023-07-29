from utils.http_methods import HttpMethods


class GoogleMapsApi:
    """Основные методы для тестирования Google Maps API"""

    base_url = "https://rahulshettyacademy.com"  # Базовая URL
    key = "?key=qaclick123"  # Параметр для всех запросов

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
        post_url = GoogleMapsApi.base_url + post_resource
        print(post_url)
        response_post = HttpMethods.post(url=post_url, body=json_for_create_new_place)
        print(response_post.text)
        return response_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки новой локации"""
        get_resource = '/maps/api/place/get/json'  # ресурс метода GET
        get_url = GoogleMapsApi.base_url + get_resource + GoogleMapsApi.key + '&place_id=' + place_id
        print(get_url)

        response_get = HttpMethods.get(url=get_url)
        print(response_get.text)
        return response_get

    @staticmethod
    def put_new_place(place_id, address):
        """Метод для изменения новой локации"""
        put_resource = '/maps/api/place/update/json'  # ресурс метода PUT
        put_url = GoogleMapsApi.base_url + put_resource + GoogleMapsApi.key + '&place_id=' + place_id
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": address,
            "key": "qaclick123"
        }
        response_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(response_put.text)
        return response_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления новой локации"""
        delete_resource = '/maps/api/place/delete/json'  # ресурс метода DELETE
        delete_url = GoogleMapsApi.base_url + delete_resource + GoogleMapsApi.key
        print(delete_url)

        json_for_delete_new_location = {"place_id": place_id}
        response_put = HttpMethods.put(delete_url, json_for_delete_new_location)
        print(response_put.text)
        return response_put



