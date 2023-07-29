import requests


def test_save_character_names_star_wars():
    """Сохранение имен всех персонажей, которые снимались в фильмах с Дарт Вейдером, в тестовый файл"""
    get_url_darth_vader = "https://swapi.dev/api/people/4/"
    response = requests.get(get_url_darth_vader)
    list_films_darth_vader = response.json()['films']  # получение списка фильмов с Darth Vader
    print("\nфильмы с Darth Vader -", list_films_darth_vader)
    list_character = []  # ссылки на персонажей

    """Получение информации о фильмах с Darth Vader и получение ссылок на персонажей этих фильмов"""
    for i in list_films_darth_vader:
        response_films = requests.get(i)  # получение информации о фильмах с Darth Vader
        list_character_films = response_films.json()['characters']  # получение списка ссылок на персонажей фильма
        print("\nсписок ссылок на персонажей фильма - ", list_character_films)

        for character_film in list_character_films:  # проверка дубликатов ссылок на персонажей
            if character_film not in list_character:
                list_character.append(character_film)  # добавление ссылки на персонажа
                # print("добавлена ссылка на персонажа -", character_film)

    """Получение имени персонажа и запись в файл"""
    for character in list_character:
        response_character = requests.get(character)  # получение информации о персонаже

        name_character = response_character.json()['name']  # получение имени персонажа

        file = open("name_character.txt", "a+", encoding="utf-8")  # Запись имен персонажей в файл
        file.write(f"{name_character}\n")
        file.close()

