"""Module to handel data."""

from typing import Type
from pydantic import BaseModel
from data.file_handler import FileHandler
from data.json_handler import JsonHandler
from data.validation_handler import ValidationHandler

class DataHandler:
    """A Common class to handel underlying data"""
    __data: object

    @classmethod
    def get_data(cls):
        """Getter for data"""
        return cls.__data

    @classmethod
    def set_data(cls , data):
        """Setter for data"""
        cls.__data = data

    @classmethod
    def load_data(cls, schema: Type[BaseModel]):
        """Method to load the data """
        file_data = FileHandler.read_data()
        json_data = JsonHandler.deserialize_json(file_data)
        cls.set_data(ValidationHandler.validate_data(json_data, schema))


