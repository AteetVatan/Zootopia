"""Module to handle File Operations."""
import os  # The os module


class FileHandler:
    """
    Class for file operations.
    """
    __file_name = "animals_data.json"
    __directory = ""

    def __init__(self, file_name: str, directory: str):
        self.__file_name = file_name
        self.__directory = directory

    @property
    def file_name(self):
        """Getter for File name."""
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name: str):
        """Setter for the File name."""
        self.__file_name = file_name

    @property
    def filepath(self):
        """Compute and return the Absolute File Path dynamically."""
        return FileHandler.__create_filepath(self.__directory, self.__file_name)

    @staticmethod
    def __create_filepath(file_dir: str, file_name: str):
        """Compute and return the Absolute File Path dynamically."""
        return str(os.path.join(os.getcwd(), file_dir, file_name))

    def read_data(self) -> str:
        """
        Method to read file data.
        :return: File data as string
        """
        d = None
        try:
            with open(self.filepath, mode="rt", encoding="utf-8") as file:
                d = file.read()
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("FileHandler.read_data - I/O error occurred: ", os.strerror(e.errno))
        return d

    def read_data_lines(self) -> list[str]:
        """
        Method to read file data.
        :return: File data as string
        """
        d = None
        try:
            with open(self.filepath, mode="rt", encoding="utf-8") as file:
                d = file.readlines()
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("FileHandler.read_data - I/O error occurred: ", os.strerror(e.errno))
        return d

    def write_data(self, file_data: str, file_dir: str = "", file_name: str = ""):
        """
        Method to write file data.
        :param file_dir: 
        :param data: data as string or list.
        :param dir: (optional)The Writable File Directory.
        :param file_name: (optional):The Writable File Name.
        """
        if file_name != "":
            filepath = FileHandler.__create_filepath(file_dir, file_name)
        else:
            filepath = self.filepath

        try:
            with open(filepath, mode="wt", encoding="utf-8") as file:
                file.write(file_data)
        except IOError as e:
            print("FileHandler.write_data - I/O error occurred: ", os.strerror(e.errno))
