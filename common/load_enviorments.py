"""Module to load the environment parameters."""
import os
from dotenv import load_dotenv


class LoadEnvironment:
    """Class to load the environment parameters."""
    __ENV_ANIMALS_API_KEY_ID = "ANIMALS_API_KEY_NAME"
    __ENV_ANIMALS_API_VALUE_ID = "ANIMALS_API_KEY_VALUE"
    __animals_api_key_name = ""
    __animals_api_key_value = ""

    def __init__(self):
        load_dotenv()
        self.load_animals_api_environment()

    @property
    def animal_api_key_name(self):
        """Animal API Key"""
        return self.__animals_api_key_name

    @property
    def animal_api_key_value(self):
        """Animal API Key Value"""
        return self.__animals_api_key_value

    def load_animals_api_environment(self):
        """Method to Load Environment Variables"""
        self.__animals_api_key_name = os.getenv(self.__ENV_ANIMALS_API_KEY_ID)
        self.__animals_api_key_value = os.getenv(self.__ENV_ANIMALS_API_VALUE_ID)
