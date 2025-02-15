"""Module for file data model"""
import config


class FileDataModel:
    """Class for file data model"""
    __slots__ = ("__file_name", "__file_dir")

    def __init__(self, file_name=None, file_dir=None):
        self.__file_name = file_name if file_name else config.ANIMALS_JSON_DATA_FILE
        self.__file_dir = file_dir if file_dir is not None else config.ANIMALS_JSON_DATA_FILE_DIR

    @property
    def file_name(self):
        """ Method to get file_name."""
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        """ Method to set file_name."""
        self.__file_name = file_name

    @property
    def file_dir(self):
        """ Method to get file_dir."""
        return self.__file_dir

    @file_dir.setter
    def file_dir(self, file_dir):
        """ Method to set file_dir."""
        self.__file_dir = file_dir
