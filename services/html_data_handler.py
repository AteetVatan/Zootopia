"""Module to handel Web data rendering."""
from services.base_data_handler import BaseDataHandler
from models.file_data_model import FileDataModel


class HtmlDataHandler(BaseDataHandler):
    """A Common class to handel underlying data"""

    def __init__(self, file_name: str, file_dir: str):
        super().__init__(FileDataModel(file_name=file_name, file_dir=file_dir))

    def __load_data(self):
        """Method to load the data """
        self.data = self.__file_handler.read_data_lines()
