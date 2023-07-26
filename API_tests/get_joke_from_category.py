import requests

# 1. Запросить у пользователя категорию, на которую он хочет получить шутку (не сами сохранить в переменную,
# а через input() и ввести в терминале
#
# 2. Отправить запрос для получения всех категорий
#
# 3. убедиться что данная категория (из пункта 1) есть в ответе запроса (отправленного в пункте 2)
#
# 4. Отправить запрос для получения шутки, которую запросил пользователь

class GetJoke:
    def test_get_one_joke_from_input_category(self, input_category):
        """получить_одну_шутку_из_вводной_категории"""
        response = requests.get("https://api.chucknorris.io/jokes/categories")  # запрос для получения всех категорий
        list_category = response.json()
        print(f"\nСписок категорий - {list_category}\n")

        assert response.status_code == 200, "Wrong status code"

        if input_category in list_category:  # убедиться что данная категория есть в ответе запроса
            print("Такая категория есть!")
            params = {"category": input_category}
            response_2 = requests.get("https://api.chucknorris.io/jokes/random", params=params)
            print(f"Шутка -  {response_2.json()['value']} \nИз категории - {response_2.json()['categories']},\n")

            assert response_2.status_code == 200, "Wrong status code"
            assert response_2.json()['categories'] == [input_category], "Wrong joke category"
        else:
            print(f"Категории '{input_category}' не найдено, попробуйте еще раз")


input_category = str(input("\nВведите категорию - "))
test_get_joke = GetJoke()
test_get_joke.test_get_one_joke_from_input_category(input_category)
