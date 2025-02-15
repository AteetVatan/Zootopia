"""Module for Animal data web interface."""
from services.html_data_handler import HtmlDataHandler
from services.data_query import DataQuery
import config


class AnimalWebGenerator:
    """Class For Animal Data HTML operation"""
    __data_handler: HtmlDataHandler
    _HTML_PLACEHOLDER = config.ANIMAL_HTML_PLACEHOLDER

    def __init__(self):
        self.__data_handler = (
            HtmlDataHandler(config.ANIMALS_HTML_TEMPLATE, config.ANIMALS_HTML_TEMPLATE_DIR))
        self.__search_keys = config.JSON_DATA_SEARCH_KEYS

    def display_key_info_in_html(self, json_data, file_name=None, title_key=None) -> None:
        """Method to display the data keys result in HTML."""
        dq = DataQuery(json_data)
        results = dq.query_data(*self.__search_keys)
        title_key = title_key if title_key is not None else self.__search_keys[0]

        key_html_list = AnimalWebGenerator._get_key_results_html(title_key, results)
        modified_html = (AnimalWebGenerator.
                         _modify_html_with_key_result(self.__data_handler.data, key_html_list))

        file_name = file_name if file_name is not None else config.ANIMALS_HTML_FILE
        self.__data_handler.write_data(modified_html, "", file_name)
        print("done")

    @staticmethod
    def _modify_html_with_key_result(html_data, key_html) -> str:
        """
        Function to print the keys in data
        :param data: The pydantic data object.
        :param keys: Searched keys tuple.
        """
        return html_data.replace(AnimalWebGenerator._HTML_PLACEHOLDER, key_html)

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
