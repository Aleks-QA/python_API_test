import json
import allure


class Assertions:
    """Methods for verifying responses"""

    @staticmethod
    def assert_status_code(response, expected_status_code):
        """Comparison of the actual code status with the expected value"""
        with allure.step(f"Comparison of the actual code status with the expected value '{expected_status_code}'"):
            assert response.status_code == expected_status_code, \
                f"\nUnexpected status code! Expected: '{expected_status_code}', Actual '{response.status_code}'\n"
            print(f"Success, expected status code received: '{expected_status_code}' == '{response.status_code}'")

    @staticmethod
    def assert_json_has_key(response, field_name):
        """Checking for the presence of a key in a JSON response"""
        with allure.step(f"Checking for the presence of a key '{field_name}' in a JSON response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert field_name in response_as_dict, f"\nResponse JSON doesn't have key '{field_name}'\n"
            print(f"Success, the response JSON has the required key: '{field_name}'")

    @staticmethod
    def assert_json_has_keys(response, names: list):
        """Checking for keys in the JSON response"""
        with allure.step(f"Checking for '{names}' keys in the JSON response"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            for name in names:
                assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"
            print(f"Success, the response JSON has the required keys: '{names}'")

    @staticmethod
    def assert_json_value_by_name(response, field_name, expected_value):  # Name - ключ по которому ищем
        """Comparison of the actual value with the expected value"""
        with allure.step(f"Comparison of the actual value with the expected value: key value '{field_name}' == '{expected_value}'"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert field_name in response_as_dict, f"\nResponse JSON doesn't have key '{field_name}'\n"
            error_massage_return = "Error, actual value does not match the expected value" + ': ' + \
                                   str(response_as_dict[field_name]) + ' != ' + str(expected_value)

            assert response_as_dict[field_name] == expected_value, error_massage_return
            print(f"Success, expected value received: '{expected_value}' == '{response_as_dict[field_name]}'")

    @staticmethod
    def assert_json_search_word_in_value(response, field_name, search_word):  # Name - ключ по которому ищем
        """Checking for the presence of a word in a field from the response"""
        with allure.step(f"Checking for the presence of a word in a field from the response: search word - {search_word}"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert field_name in response_as_dict, f"\nResponse JSON doesn't have key '{field_name}'\n"
            error_massage_return = "Error, the received value does not contain the required word" + ': ' + \
                                   str(response_as_dict[field_name]) + ' not included ' + str(search_word)

            assert search_word in response_as_dict[field_name], error_massage_return
            print(f"Success, the received value contains the required word: '{response_as_dict[field_name]}' contains '{search_word}'")


