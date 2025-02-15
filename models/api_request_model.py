""" Module for API Request Model."""
import config
from common.load_enviorments import LoadEnvironment


class ApiRequestModel:
    """ Class for API Request Model."""
    __api_base_url = __key_name = __key_value = ""
    __query_endpoint = __query_param_key = ""

    def __init__(self):
        env = LoadEnvironment()
        self.__api_base_url = config.ANIMAL_API_BASE_URL
        self.__key_name = env.animal_api_key_name
        self.__key_value = env.animal_api_key_value
        self.__query_endpoint = config.ANIMAL_API_QUERY_ENDPOINT
        self.__query_param_key = config.ANIMAL_API_QUERY_PARAM_NAME
        self.__query_param_value = "fox"

    @property
    def endpoint_url(self):
        """ Method to get endpoint_url."""
        return f"{self.__api_base_url}{self.__query_endpoint}"

    @property
    def param_dict(self):
        """ Method to get the HTTP get request query parameter dictionary."""
        return {self.__query_param_key: self.__query_param_value}

    @property
    def header_dict(self):
        """ Method to get the HTTP get request header dictionary ."""
        return {self.__key_name: self.__key_value}

    @property
    def api_base_url(self):
        """ Method to api base URL."""
        return self.__api_base_url

    @property
    def key_name(self):
        """ Method to API Key Name in config file."""
        return self.__key_name

    @property
    def key_value(self):
        """ Method to API Key Value Name in config file."""
        return self.__key_value

    @property
    def query_endpoint(self):
        """ Method to get the Http request Query end point."""
        return self.__query_endpoint

    @property
    def query_param_key(self):
        """ Method to get query_param_key."""
        return self.__query_param_key

    @property
    def query_param_value(self):
        """ Method to get query_param_value."""
        return self.__query_param_value

    @query_param_key.setter
    def query_param_value(self, value):
        """ Method to set query_param_value."""
        self.__query_param_value = value
