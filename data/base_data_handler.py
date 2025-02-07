"""Module specifying abstract base class for data operations."""

from data.file_handler import FileHandler


class BaseDataHandler():
    """Base class to handel underlying data"""
    __data: object
    __file_name: str
    __file_dir: str
    __file_handler: FileHandler

    def __init__(self, file_name: str, file_dir: str):
        self.__file_name = file_name
        self.__file_dir = file_dir
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
        """Method to load the data """
        self.data = self.__file_handler.read_data()

    def write_data(self, file_data: str, file_dir: str = "", file_name: str = ""):
        """Method to write the data """
        self.data = self.__file_handler.write_data(file_data,
                                                   file_dir=file_dir, file_name=file_name)
