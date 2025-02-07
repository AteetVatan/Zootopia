"""Module to handel Web data rendering."""
from data.base_data_handler import BaseDataHandler


class HtmlDataHandler(BaseDataHandler):
    """A Common class to handel underlying data"""

    def __init__(self, file_name: str, file_dir: str):
        super().__init__(file_name, file_dir)

    def __load_data(self):
        """Method to load the data """
        self.data = self.__file_handler.read_data_lines()
