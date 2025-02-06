"""Module for Json DeSerialization"""
import json  # json module for json


class JsonHandler:

    @classmethod
    def deserialize_json(cls, jason_str: str):
        """
        Method to Json DeSerialization to the given schema class instance.
        :param jason_str: The Json data string
        :param schema: Type[BaseModel] this checks schema must be a class that inherits from BaseModel
        :return:
        """
        try:
            json_data = json.loads(jason_str)
            return json_data
        except json.JSONDecodeError as e:
            print(f"JsonHandler.deserialize_json : JSONDecodeError - {e}")
