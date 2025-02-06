"""THe Main Zootopia Module"""
from typing import Type

from data.data_handler import DataHandler
from data.animal_metadata_schema import *
from data.data_query import DataQuery


def init_zootopia():
    dh = DataHandler(AnimalMetadataSchemaRoot)
    data = dh.data
    search_keys = ("name", "diet", "locations", "type")
    find_and_print(data, search_keys)


def find_and_print(data: Type[BaseModel], args):
    """
    Function to print the keys in data
    :param data: The pydantic data object.
    :param args: Searched keys tuple.
    """
    dq = DataQuery(data)
    results = dq.query_data(*args)
    for item in results:
        for k, v in item.items():
            if type(v) is list:
                val = str(v[0])
            else:
                val = str(v)
            print(f"{k.title()}: {val.title()}")
        print()


if __name__ == "__main__":
    init_zootopia()
