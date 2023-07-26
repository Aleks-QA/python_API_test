from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Тест-кейсы"""

    def test_create_new_place(self):
        """Создание, изменение и удаление новой локации"""
        print("\nМетод POST")
        response_post = GoogleMapsApi.create_new_place()
        check_post = response_post.json()
        place_id = check_post["place_id"]
        print('place_id - ', place_id)

        print("\nМетод GET POST")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)

        print("\nМетод PUT")
        response_put = GoogleMapsApi.put_new_place(place_id=place_id, address="New York")

        print("\nМетод GET PUT")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)

        print("\nМетод DELETE")
        response_delete = GoogleMapsApi.delete_new_place(place_id=place_id)

        print("\nМетод GET DELETE")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)










