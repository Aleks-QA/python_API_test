import requests


class TestNewJoke:
    """"""
    def __init__(self):
        pass

    def get_random_joke(self):
        """get_random_joke"""
        data = {}
        params = {}
        headers = {}
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url, params=params, headers=headers, data=data)
        response.encoding = "utf-8"  # для надежности
        print(response.json()["value"])

        response_json = response.json()
        print(response_json.get("value"))


random_joke = TestNewJoke()
random_joke.get_random_joke()

