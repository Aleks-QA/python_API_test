import json
import pytest
import requests

# 1. Отправить метод POST
#
# 2. Создать текстовый файл в котором хранить 5 шт place_id полученных из 1 пункта (не писать портянку вызывая 5
# раз метод, сделать красиво)
#
# 3. Отправить метод Get который будет читать place_id из текстового файла (из него, не их переменной первого запроса)
# и убедиться что данные place_id существуют

class TestCreateLocation:
    base_url = "https://rahulshettyacademy.com"
    number = [0, 1, 2, 3, 4]

    @pytest.mark.parametrize('number', number)  # используется вместо цикла и для построчного чтения из файла
    def test_create_new_location_and_write_place_id_to_file(self, number):
        """Создание текстового файла в котором хранятся place_id"""
        resource = "/maps/api/place/add/json"
        post_url = self.base_url + resource

        params = {"key": "qaclick123"}
        data = json.dumps({
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Front house",
            "phone_number": "(+91) 983 893 3937",
            "address": f'street 1{number}',
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        })

        response = requests.post(post_url, params=params, data=data)
        assert 200 == response.status_code, "place creation error"
        print("Успешно!!! Создана новая локация", '\n', response.json(), '\n')

        # Запись place_id в файл
        place_id = response.json()['place_id']
        file = open("list_place_id.txt", "a+")
        file.write(f'{place_id}\n')
        file.close()

    @pytest.mark.parametrize('number', number)
    def test_availability_place_id(self, number):
        """Проверка, что place_id из текстового файла существуют"""
        with open("list_place_id.txt", "r") as f:
            # Чтение place_id из файла с определенной строки
            text = f.readlines()
            check_place_id = text[number].splitlines()  # возвращает текст из файла без разрывов

        params = {"key": "qaclick123", "place_id": check_place_id}

        resource = "/maps/api/place/get/json"
        get_url = self.base_url + resource
        response = requests.get(get_url, params=params)

        assert response.status_code == 200, "Wrong status code"
        print(response.json(), '\n')

        # if number == 4:
        #     # Очистка файла после тестов
        #     f = open('list_place_id.txt', 'w')
        #     f.close()

