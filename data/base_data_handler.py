"""Module specifying abstract base class for data operations."""

from data.file_handler import FileHandler
from data.api_handler import ApiHandler


class BaseDataHandler():
    """Base class to handel underlying data"""
    __data: object
    __file_name: str
    __file_dir: str
    __file_handler: FileHandler
    __api_handler: ApiHandler
    __load_data_from_api = False

    # api_tup = (api_base_url,key_name,key_value,query_endpoint, query_param_key, query_param_value)
    def __init__(self, file_tup: (str, str) = None, load_data_from_api = False):
        self.__load_data_from_api = load_data_from_api
        if load_data_from_api:
            # env object
            self.__api_handler = ApiHandler()
            self.__data_from_api = True
        else:
            self.__file_name = file_tup[0]
            self.__file_dir = file_tup[1]
            self.__file_handler = FileHandler(self.__file_name, self.__file_dir)

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
            self.data = self.__api_handler.get_data("cat")

    def write_data(self, file_data: str, file_dir: str = "", file_name: str = ""):
        """Method to write the data """
        self.data = self.__file_handler.write_data(file_data,
                                                   file_dir=file_dir, file_name=file_name)
