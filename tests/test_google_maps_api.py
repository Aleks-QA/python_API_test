from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    """Создание, изменение и удаление новой локации"""

    def test_create_new_place(self):

        print("\nМетод POST")
        response_post: Response = GoogleMapsApi.create_new_place()









