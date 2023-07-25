import json

import requests


class TestCreateLocation:
    """"""

    def test_create_new_location(self):
        base_url = "https://rahulshettyacademy.com"
        resourse = "/maps/api/place/add/json"

        post_url = base_url + resourse

        params = {"key": "qaclick123",
                  "Content-Type": "application/json"}
        data = json.dumps({  # json.dumps
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        })

        response = requests.post(post_url, params=params, data=data)
        t = response.text
        text = json.dumps(t, sort_keys=True, indent=4)
        print(text)
        assert 200 == response.status_code
        print("Успешно!!! Создана новая локация")


