"""Module to handle File Operations."""
import os  # The os module


class FileHandler:
    """
    Class for file operations.
    """
    __file_name = "animals_data.json"

    @classmethod
    def get_file_name(cls):
        """Getter for File name."""
        return cls.__file_name

    @classmethod
    def set_file_name(cls, file_name: str):
        """Setter for the File name."""
        cls.__file_name = file_name

    @classmethod
    def get_filepath(cls):
        """Compute and return the Absolute File Path dynamically."""
        return str(os.path.join(os.getcwd(), "data", cls.__file_name))  # ✅ Compute dynamically


    @classmethod
    def read_data(cls):
        """
        Method to read file data.
        :return: File data as string
        """
        d = None
        try:
            with open(cls.get_filepath(), mode="rt", encoding="utf-8") as data:  # ✅ Now file_path is a computed property
                d = data.read()
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("FileHandler.read_data - I/O error occurred: ", os.strerror(e.errno))
        return d
