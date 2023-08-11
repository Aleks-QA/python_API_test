import allure
from utils.assertions import Assertions
import requests


@allure.epic("Preserving the names of characters who starred alongside Darth Vader 'swapi.dev'")
def test_save_character_names_star_wars():
    """ Сохранение имен всех персонажей, которые снимались в фильмах с Дарт Вейдером, в текстовый файл """

    with allure.step(f"Getting a list of Darth Vader movies"):
        get_url_darth_vader = "https://swapi.dev/api/people/4/"  # url с информацией о персонаже Дарт Вейдер
        response = requests.get(get_url_darth_vader)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'films')

        list_films_darth_vader = response.json()['films']  # получение списка фильмов с Darth Vader
        print("\nфильмы с Darth Vader -", list_films_darth_vader)

    with allure.step(f"Getting references to the characters in these movies"):
        """Получение информации о фильмах с Darth Vader и получение ссылок на персонажей этих фильмов"""
        list_character = []  # ссылки на персонажей
        for i in list_films_darth_vader:
            response_films = requests.get(i)  # получение информации о фильмах с Darth Vader
            Assertions.assert_status_code(response_films, 200)
            Assertions.assert_json_has_key(response_films, 'characters')

            list_character_films = response_films.json()['characters']  # получение списка ссылок на персонажей фильма
            print("\nсписок ссылок на персонажей фильма - ", list_character_films)

            for character_film in list_character_films:  # проверка дубликатов ссылок на персонажей
                if character_film not in list_character:
                    list_character.append(character_film)  # добавление ссылки на персонажа

    with allure.step(f"Getting a character name and writing it to a file"):
        """Получение имени персонажа и запись в файл"""
        for character in list_character:
            response_character = requests.get(character)  # получение информации о персонаже
            Assertions.assert_status_code(response_character, 200)
            Assertions.assert_json_has_key(response_character, 'name')

            name_character = response_character.json()['name']  # получение имени персонажа

            file = open("name_character.txt", "a+", encoding="utf-8")  # Запись имен персонажей в файл
            file.write(f"{name_character}\n")
            file.close()
