import allure
from utils.api import GoogleMapsApi
from utils.assertions import Assertions


@allure.epic("Test create place 'Google Maps API'")
class TestCreatePlace:
    """Проверка создания локаций Google Maps API"""

    @allure.description("Creating, modifying and deleting a new location")
    def test_create_new_place(self):
        """Создание, изменение и удаление новой локации"""

        print("\nМетод POST - создание новой локации")
        response_post = GoogleMapsApi.create_new_place()
        check_post = response_post.json()
        place_id = check_post["place_id"]
        print('place_id - ', place_id)
        Assertions.assert_status_code(response_post, 200)
        expected_keys = ['place_id', 'status', 'scope', 'reference', 'id']
        Assertions.assert_json_has_keys(response_post, expected_keys)
        Assertions.assert_json_value_by_name(response_post, "status", 'OK')

        print("\nМетод GET POST - проверка создания новой локации")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)
        Assertions.assert_status_code(response_get, 200)
        expected_keys = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        Assertions.assert_json_has_keys(response_get, expected_keys)
        Assertions.assert_json_value_by_name(response_get, "address", 'street')

        print("\nМетод PUT - изменение новой локации")
        response_put = GoogleMapsApi.put_new_place(place_id=place_id, address="New York")
        Assertions.assert_status_code(response_put, 200)
        expected_keys = ["msg"]
        Assertions.assert_json_has_keys(response_put, expected_keys)
        Assertions.assert_json_value_by_name(response_put, "msg", 'Address successfully updated')

        print("\nМетод GET PUT - проверка изменения новой локации")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)
        Assertions.assert_status_code(response_get, 200)
        expected_keys = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language']
        Assertions.assert_json_has_keys(response_get, expected_keys)
        Assertions.assert_json_value_by_name(response_get, "address", 'New York')

        print("\nМетод DELETE - удаление созданной локации")
        response_delete = GoogleMapsApi.delete_new_place(place_id=place_id)
        Assertions.assert_status_code(response_delete, 200)
        expected_keys = ['status']
        Assertions.assert_json_has_keys(response_delete, expected_keys)
        Assertions.assert_json_value_by_name(response_delete, "status", 'OK')

        print("\nМетод GET DELETE - проверка удаления созданной локации")
        response_get = GoogleMapsApi.get_new_place(place_id=place_id)
        Assertions.assert_status_code(response_get, 404)
        expected_keys = ["msg"]
        Assertions.assert_json_has_keys(response_get, expected_keys)
        Assertions.assert_json_search_word_in_value(response_get, "msg", "failed")
