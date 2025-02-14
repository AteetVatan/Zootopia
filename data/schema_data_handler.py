"""Module to handel data."""

from typing import Type
from pydantic import BaseModel
from data.base_data_handler import BaseDataHandler
from data.json_helper import JsonHelper
from data.validation_handler import ValidationHandler


class SchemaDataHandler(BaseDataHandler):
    """Class to handel underlying data loading and validations"""

    # file_tup = (file_name, file_dir) or api_tup = ("api_name")
    def __init__(self, schema: Type[BaseModel], file_tup: (str, str) = None, load_data_from_api=False):
        # if file_tup:
        super().__init__(file_tup, load_data_from_api)
        self.__schema_process(schema)

    def __schema_process(self, schema: Type[BaseModel]):
        """Method to deserialize json data and validate/cast to given schema"""
        if isinstance(self.data, str):
            self.data = JsonHelper.deserialize_json(self.data)  # load json data.

        chk = str(self.data)
        # Schema Validation for json data and serialize to schema class
        self.data = ValidationHandler.validate_and_serialize_data_to_schema(self.data, schema)
