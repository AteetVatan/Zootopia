import requests
from models.api_request_model import ApiRequestModel


class ApiHandler:
    __api_request_model: ApiRequestModel

    def __init__(self):
        self.__api_request_model = ApiRequestModel()

    def get_data(self, query_param_value):
        api_url = self.__api_request_model.get_endpoint_url
        params = self.__api_request_model.get_param_dict(query_param_value)
        headers = self.__api_request_model.get_request_header_dict
        response = ApiHandler.__get_request_with_params(api_url, params=params, headers=headers)

        try:
            if response.status_code != requests.codes.ok:
                raise ValueError("Error:", response.status_code, response.text)

            return response.json()
        except ValueError:
            return {"error": "Invalid JSON response"}

    @staticmethod
    def __get_request_with_params(url, params=None, headers=None):
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            return {"error": "Request timed out"}
        except requests.exceptions.ConnectionError:
            return {"error": "Failed to connect to the server"}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"An error occurred: {err}"}
