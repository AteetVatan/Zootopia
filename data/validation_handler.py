"""Module for Data Validation."""
import sys
from typing import Type  # typing module for specifying Explicit types.
from pydantic import BaseModel, ValidationError  # pydantic module for schema validation.


class ValidationHandler:
    """Class for Data Validation."""

    @classmethod
    def validate_and_serialize_data_to_schema(cls, data: object, schema: Type[BaseModel]):
        """
        Method to validate data with given schema and serialize it to the
        schema class object.
        :param data: The generic data object(can be of any type).
        :param schema: Type[BaseModel] this checks schema must be a class
        that inherits from BaseModel.
        :return: schema object
        """
        try:
            validated_data = schema.model_validate(data)
            return validated_data
        except ValidationError as e:
            errors = e.errors()
            print(f"ValidationHandler.Validation Error: ")
            for err in errors:
                print(f"{err}")
            sys.exit(1)

    @classmethod
    def set_schema(cls):
        """Method to set Schema."""
        return False
