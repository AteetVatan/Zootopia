"""Module specifying abstract base class for data operations."""

from abc import ABC

from helpers.file_helper import FileHelper
from helpers.api_helper import ApiHelper
from models.file_data_model import FileDataModel
from models.api_request_model import ApiRequestModel


class BaseDataHandler(ABC):
    """Base class to handel underlying data"""
    __data: object
    __file_handler: FileHelper
    __file_data_model: FileDataModel
    __api_handler: ApiHelper
    __api_request_model: ApiRequestModel

    # api_tup = (api_base_url,key_name,key_value,query_endpoint, query_param_key, query_param_value)
    def __init__(self, file_data_model: FileDataModel = None,
                 api_request_model: ApiRequestModel = None,
                 load_data_from_api=False):
        self.__load_data_from_api = load_data_from_api
        if load_data_from_api:
            self.__api_request_model = api_request_model if api_request_model else ApiRequestModel()
            self.__api_handler = ApiHelper(self.__api_request_model)
        else:
            self.__file_data_model = file_data_model if file_data_model else FileDataModel()
            self.__file_handler = FileHelper(self.__file_data_model)

        self.__load_data()

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, data):
        """Setter for data"""
        self.__data = data

    def __load_data(self):
        """Method to load the file data """
        if not self.__load_data_from_api:
            self.data = self.__file_handler.read_data()
        else:
            self.data = self.__api_handler.get_data()

    def write_data(self, file_data: str, file_dir: str = "", file_name: str = ""):
        """Method to write the data """
        self.data = self.__file_handler.write_data(file_data,
                                                   file_dir=file_dir, file_name=file_name)
