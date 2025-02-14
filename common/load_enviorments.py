import os
from dotenv import load_dotenv


class LoadEnvironment:
    __ENV_ANIMALS_API_KEY_ID = "ANIMALS_API_KEY_NAME"
    __ENV_ANIMALS_API_VALUE_ID = "ANIMALS_API_KEY_VALUE"
    __ANIMALS_API_KEY_NAME = ""
    __ANIMALS_API_KEY_VALUE = ""

    def __init__(self):
        chk = load_dotenv()
        self.load_animals_api_environment()

    @property
    def animal_api_key_name(self):
        return self.__ANIMALS_API_KEY_NAME

    @property
    def animal_api_key_value(self):
        return self.__ANIMALS_API_KEY_VALUE

    def load_animals_api_environment(self):
        self.__ANIMALS_API_KEY_NAME = os.getenv(self.__ENV_ANIMALS_API_KEY_ID)
        self.__ANIMALS_API_KEY_VALUE = os.getenv(self.__ENV_ANIMALS_API_VALUE_ID)
