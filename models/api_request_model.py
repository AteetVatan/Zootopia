# (api_base_url,key_name,key_value,query_endpoint, query_param_key, query_param_value)
import config
from common.load_enviorments import LoadEnvironment


class ApiRequestModel:
    __api_base_url = __key_name = __key_value = ""
    __query_endpoint = __query_param_key = ""
    __env_obj = LoadEnvironment()

    def __init__(self):
        env = LoadEnvironment()
        self.__api_base_url = config.ANIMAL_API_BASE_URL
        self.__key_name = env.animal_api_key_name
        self.__key_value = env.animal_api_key_value
        self.__query_endpoint = config.ANIMAL_API_QUERY_ENDPOINT
        self.__query_param_key = config.ANIMAL_API_QUERY_PARAM_NAME
        self.__query_param_value = "fox"

    @property
    def get_endpoint_url(self):
        return f"{self.__api_base_url}{self.__query_endpoint}"

    def get_param_dict(self, query_param_value = "fox"):
        return {self.__query_param_key: query_param_value}

    @property
    def get_request_header_dict(self):
        return {self.__key_name: self.__key_value}
