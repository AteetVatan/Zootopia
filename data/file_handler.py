"""Module to read and write data"""
import os


class FileHandler:
    __json_file_name = "animals_data.json"
    __json_file_path = os.path.join(os.getcwd(), "data", __json_file_name)

    @classmethod
    @property
    def json_file_name(cls):
        """Method to get Json file name"""
        return cls.__json_file_name

    @classmethod
    def read_data(cls):
        """Method to read data fo file"""
        d = None
        try:
            with open(cls.__json_file_path, mode="+rt", encoding="utf-8") as data:
                d = data.read()
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("FileHandler.read_data - I/O error occurred: ", os.strerror(e.errno))
        return d
