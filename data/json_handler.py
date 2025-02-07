"""Module for Json Operations."""
import json  # json module for json


class JsonHandler:
    """Class for Json Deserialization and Serialization"""

    @classmethod
    def deserialize_json(cls, jason_str: str):
        """
        Method for Json Deserialization to the given schema class instance.
        :param jason_str: The Json data string.
        :return: Deserialized Json Data object.
        """
        try:
            json_data = json.loads(jason_str)
        except json.JSONDecodeError as e:
            print(f"JsonHandler.deserialize_json : JSONDecodeError - {e}")
            json_data = None
        return json_data

    @classmethod
    def serialize_json(cls, obj: object):
        """
        Method for Json Serialization 
        :param obj: The data obj.
        :return:
        """
        return obj
