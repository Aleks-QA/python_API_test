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

    def get_joke_from_sport_category(self):
        """get_joke"""
        data = {}
        params = {"category": "sport"}
        headers = {}
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url, params=params, headers=headers, data=data)
        response.encoding = "utf-8"  # для надежности
        print("value - ", response.json()["value"])
        print("categories - ", response.json()["categories"])


random_joke = TestNewJoke()
random_joke.get_random_joke()
random_joke.get_joke_from_sport_category()

