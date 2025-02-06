from typing import Type, List, Dict
from pydantic import BaseModel


class DataQuery:
    # The pydantic data object 
    _data: Type[BaseModel]

    def __init__(self, data: Type[BaseModel]):
        self._data = data

    def query_data(self, *args) -> List[Dict]:
        """
        Method to query pydentic data model
        :param args: Searched keys tuple.
        :return: List
        """
        data_list = self._data.dict()
        search_dict_list = []
        for obj in data_list:
            search_dict = {}
            for key in args:
                val = self.__search_key(obj, key)
                if val:
                    search_dict[key] = val
            search_dict_list.append(search_dict.copy())
        return search_dict_list

    def __search_key(self, model: BaseModel, key: str):
        """
        Recursively searches for a key value in pydantic data object.
        """
        if isinstance(model, BaseModel):
            model_dict = model.dict()
        elif isinstance(model, dict):
            model_dict = model
        elif isinstance(model, list):
            for item in model:
                result = self.__search_key(item, key)
                if result is not None:
                    return result
            return None
        else:
            return None

        for k, v in model_dict.items():
            if k == key:
                return v
            if isinstance(v, (dict, list, BaseModel)):
                result = self.__search_key(v, key)
                if result is not None:
                    return result
        return None
