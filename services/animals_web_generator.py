"""Module for Animal data web interface."""
from typing import List, Dict
from services.html_data_handler import HtmlDataHandler
from services.data_query import DataQuery
import config
from constants import constants


class AnimalWebGenerator:
    """Class For Animal Data HTML operation"""
    __data_handler: HtmlDataHandler
    _HTML_PLACEHOLDER = config.ANIMAL_HTML_PLACEHOLDER
    __query_data = None

    def __init__(self):
        self.__data_handler = (
            HtmlDataHandler(config.ANIMALS_HTML_TEMPLATE, config.ANIMALS_HTML_TEMPLATE_DIR))
        self.__search_keys = config.JSON_DATA_SEARCH_KEYS

    @property
    def query_data(self):
        """The Query Data."""
        return self.__query_data

    def set_query_data(self, data):
        """Method to get the data for the keys see JSON_DATA_SEARCH_KEYS."""
        if len(data.root) > 0:
            dq = DataQuery(data)
            self.__query_data = dq.query_data(*self.__search_keys)
            return
        self.__query_data = list()

    def display_key_info_in_html(self, data, file_name=None, title_key=None, search_item=None) -> bool:
        """Method to display the data keys result in HTML."""
        self.set_query_data(data)
        if len(self.__query_data) > 0:
            title_key = title_key if title_key is not None else self.__search_keys[0]
            key_html_list = AnimalWebGenerator._get_key_results_html(title_key, self.__query_data)
            modified_html = (self.__modify_html_with_key_result(key_html_list))
            success = True
        else:
            result_html = constants.HTML_NO_OUTPUT.format(search=search_item)
            modified_html = (self.__modify_html_with_key_result(result_html))
            success = False

        file_name = file_name if file_name is not None else config.ANIMALS_HTML_FILE
        self.__data_handler.write_data(modified_html, "", file_name)
        return success

    def __modify_html_with_key_result(self, html_data) -> str:
        """
        Method to print the keys in data
        :param html_data: Searched keys tuple.
        """
        return self.__data_handler.data.replace(AnimalWebGenerator._HTML_PLACEHOLDER, html_data)

    @staticmethod
    def _get_key_results_html(title_key: str, data_list: list[dict]) -> str:
        """
        Function to print the keys in data
        :param title_key: The Title Key header.
        :param data_list: The animal keys data list.
        """
        line_list = []
        for item in data_list:
            line_list.append('<li class="cards__item">\n')
            title = ""
            sub_line_list = ['<div class="card__text">\n<ul>']
            for k, v in item.items():
                if isinstance(v, list):
                    val = str(v[0])
                else:
                    val = str(v)
                if k == title_key:
                    title = f'<div class="card__title">{val.title()}</div>\n'
                else:
                    sub_line_list.append(f"<li><strong>{k.title()}:</strong> {val.title()}</li>\n")
            sub_line_list.append('</ul>\n</div>')
            line_list.append(title)
            line_list.append('<p class="card__text">')
            line_list.extend(sub_line_list)
            line_list.append('</p>')
            line_list.append('</li>\n')

        res = "".join(line_list)
        return res
