import json
import pytest
import requests

# 1. Отправить метод DELETE, с помощью которого удалить 2-й и 4-й place_id из текстового файла, полученного в
# результате выполнения предыдущего задания (удалить значит не стереть, это значит что в файле по-прежнему 5
# значений, но 2-я и 4-я локация не существуют)
#
# 2. Отправить метод Get который будет читать place_id из текстового файла, и сделает отбор на существующие и
# несуществующие локации
#
# 3. Создать новый файл и поместить в него 3 существующие локации (place_id), которые были отобраны в результате
# метода GET

class TestCreateLocation:
    base_url = "https://rahulshettyacademy.com"
    line_delete = [1, 3]

    @pytest.mark.parametrize('line_delete', line_delete)  # используется вместо цикла и для построчного чтения из файла
    def test_delete_place(self, line_delete):
        """Удаление 2 и 4 локации"""
        resource = "/maps/api/place/delete/json"
        post_url = self.base_url + resource

        with open("list_place_id.txt", "r") as f:
            # Чтение place_id из файла с определенной строки
            text = f.readlines()
            delete_place_id = text[line_delete].splitlines()  # возвращает текст из файла без разрывов, но список

        params = {"key": "qaclick123"}
        data = json.dumps({
            "place_id": delete_place_id[0]
        })

        response = requests.delete(post_url, params=params, data=data)
        assert 200 == response.status_code, "place creation error"
        print("Успешно!!! Локация удалена", '\n', response.json(), '\n')

    line_check = [0, 1, 2, 3, 4]

    @pytest.mark.parametrize('line_check', line_check)
    def test_availability_place_id(self, line_check):
        """Отбор на существующие и несуществующие локации"""
        with open("list_place_id.txt", "r") as f:
            # Чтение place_id из файла с определенной строки
            text = f.readlines()
            check_place_id = text[line_check].splitlines()  # возвращает текст из файла без разрывов

        params = {"key": "qaclick123", "place_id": check_place_id}

        resource = "/maps/api/place/get/json"
        get_url = self.base_url + resource
        response = requests.get(get_url, params=params)
        print(response.json(), '\n')

        if response.status_code == 200:
            print("----------------")
            # Запись существующих place_id в файл
            file = open("new_list_place_id.txt", "a+")
            file.write(f'{check_place_id[0]}\n')
            file.close()
