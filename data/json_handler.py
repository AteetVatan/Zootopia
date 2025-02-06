"""Module for Json DeSerialization """
import json
from pydantic import BaseModel, ValidationError
from typing import Type
from data.animal_metadata_schema import AnimalMetadataSchemaRoot


class JsonHandler:

    @classmethod
    def deserialize_json(cls, jason_str: str, schema: Type[BaseModel]):
        """
        Method to Json DeSerialization to the given schema class instance.
        :param jason_str: The Json data string
        :param schema: Type[BaseModel] this checks schema must be a class that inherits from BaseModel
        :return:
        """
        try:
            data = json.loads(jason_str)
            deserialized_data = schema.model_validate(data)
            return deserialized_data
        except json.JSONDecodeError as e:
            print(f"JsonHandler : JSONDecodeError - {e}")
        except ValidationError as e:
            print(f"JsonHandler : ValidationError - {e}")
