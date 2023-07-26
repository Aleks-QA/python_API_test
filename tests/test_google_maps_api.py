from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""

    def test_create_new_place(self):

        print("\nМетод POST")
        response_post = GoogleMapsApi.create_new_place()
        check_post = response_post.json()
        place_id = check_post["place_id"]
        print('place_id - ', place_id)

        print("\nМетод GET")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)









