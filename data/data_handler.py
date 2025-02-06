"""Module to handel data."""

from typing import Type
from pydantic import BaseModel
from data.file_handler import FileHandler
from data.json_handler import JsonHandler
from data.validation_handler import ValidationHandler


class DataHandler:
    """A Common class to handel underlying data"""
    __data: object

    def __init__(self, schema: Type[BaseModel]):
        self.__load_data(schema)

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, data):
        """Setter for data"""
        self.__data = data

    def __load_data(self, schema: Type[BaseModel]):
        """Method to load the data """
        file_data = FileHandler.read_data()
        json_data = JsonHandler.deserialize_json(file_data)
        self.data = ValidationHandler.validate_data(json_data, schema)
