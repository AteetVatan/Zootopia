"""Module to handel data."""

from typing import Type
from pydantic import BaseModel
from data.base_data_handler import BaseDataHandler
from data.json_handler import JsonHandler
from data.validation_handler import ValidationHandler


class SchemaDataHandler(BaseDataHandler):
    """Class to handel underlying data loading and validations"""

    def __init__(self, file_name: str, file_dir: str, schema: Type[BaseModel]):
        super().__init__(file_name, file_dir)
        self.__schema_process(schema)

    def __schema_process(self, schema: Type[BaseModel]):
        """Method to deserialize json data and validate/cast to given schema"""
        json_data = JsonHandler.deserialize_json(self.data)  # load json data.
        # Schema Validation for json data and serialize to schema class
        self.data = ValidationHandler.validate_and_serialize_data_to_schema(json_data, schema)
