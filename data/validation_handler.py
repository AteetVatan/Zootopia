"""Module for Data Validation."""
from pydantic import BaseModel, ValidationError  # pydantic module for schema validation.
from typing import Type  # typing module for specifying Explicit types.


class ValidationHandler:

    @classmethod
    def validate_data(cls, data: object, schema: Type[BaseModel]):
        """
        Method to validate data with given schema class instance.
        :param data: The generic data object(can be of any type).
        :param schema: Type[BaseModel] this checks schema must be a class that inherits from BaseModel.
        :return:
        """
        try:
            validated_data = schema.model_validate(data)
            return validated_data
        except ValidationError as e:
            print(f"ValidationHandler.validate_data : ValidationError - {e}")
