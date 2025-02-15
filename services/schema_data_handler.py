"""Module to handel data."""

from typing import Type
from pydantic import BaseModel
from services.base_data_handler import BaseDataHandler
from helpers.json_helper import JsonHelper
from helpers.validation_helper import ValidationHelper
import config


class SchemaDataHandler(BaseDataHandler):
    """Class to handel underlying data loading and validations"""

    # file_tup = (file_name, file_dir) or api_tup = ("api_name")
    def __init__(self, schema: Type[BaseModel]):
        # if file_tup:
        super().__init__(load_data_from_api=config.LOAD_DATA_FROM_API)
        self.__schema_process(schema)

    def __schema_process(self, schema: Type[BaseModel]):
        """Method to deserialize json data and validate/cast to given schema"""
        if isinstance(self.data, str):
            self.data = JsonHelper.deserialize_json(self.data)  # load json data.

        # Schema Validation for json data and serialize to schema class
        self.data = ValidationHelper.validate_and_serialize_data_to_schema(self.data, schema)
