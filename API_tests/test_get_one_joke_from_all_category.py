import requests


class TestGetJoke:
    def test_get_one_joke_from_all_category_(self):
        """Получить одну шутку из каждой категории"""

        response = requests.get("https://api.chucknorris.io/jokes/categories")  # получить список категорий
        list_category = response.json()
        print(f"\nСписок категорий - {list_category}\n")

        assert response.status_code == 200, "Wrong status code"

        for i in list_category:  # Получить шутку из каждой категории
            params = {"category": i}
            response = requests.get("https://api.chucknorris.io/jokes/random", params=params)
            print(f"Категория - {response.json()['categories']},\nШутка -  {response.json()['value']} \n")

            assert response.status_code == 200, "Wrong status code"
            assert response.json()['categories'] == [i], "Wrong joke category"

