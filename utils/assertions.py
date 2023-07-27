import json

import allure


class Assertions:
    """Methods for verifying responses"""

    @staticmethod
    def assert_status_code(response, expected_status_code):
        """Comparison of the actual code status with the expected value"""
        with allure.step(f"Comparison of the actual code status with the expected value '{expected_status_code}'"):
            assert response.status_code == expected_status_code, \
                f"\nUnexpected status code! Expected: {expected_status_code}, Actual {response.status_code}\n"
            print(f"Success, expected status code received - {expected_status_code}")

    @staticmethod
    def assert_json_has_key(response, name):
        """Checking for the presence of a key in a JSON response"""
        with allure.step(f"Checking for the presence of a key '{name}' in a JSON response"):
            try:

                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert name in response_as_dict, f"\nResponse JSON doesn't have key '{name}'\n"

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

    @staticmethod
    def assert_json_value_by_name(response, name_value, expected_value):  # Name - ключ по которому ищем
        """Comparison of the actual value with the expected value"""
        with allure.step(f"Comparison of the actual value with the expected value: key value '{name_value}' == '{expected_value}'"):
            try:
                response_as_dict = response.json()
            except json.JSONDecodeError:
                assert False, f"\nResponse is not in JSON format. Response text is '{response.text}'\n"

            assert name_value in response_as_dict, f"\nResponse JSON doesn't have key '{name_value}'\n"
            error_massage_return = "Error, actual value does not match the expected value" + ': ' + str(response_as_dict[name_value]) + ' != ' + str(expected_value)
            assert response_as_dict[name_value] == expected_value, error_massage_return

