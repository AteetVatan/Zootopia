"""Module for Animal data web interface."""
from data.html_data_handler import HtmlDataHandler
from data.data_query import DataQuery


class AnimalWebGenerator:
    """Class For Animal Data HTML operation"""
    __data_handler: HtmlDataHandler
    HTML_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"

    def __init__(self, file_name, file_dir):
        self.__data_handler = HtmlDataHandler(file_name, file_dir)

    def display_key_info_in_html(self, json_data, keys, title_key, file_name):
        """Method to display the data keys result in HTML."""
        dq = DataQuery(json_data)
        results = dq.query_data(*keys)
        key_html_list = AnimalWebGenerator.__get_key_results_html(title_key, results)
        modified_html = (AnimalWebGenerator.
                         __modify_html_with_key_result(self.__data_handler.data, key_html_list))
        self.__data_handler.write_data(modified_html, "", file_name)
        print("done")

    @staticmethod
    def __modify_html_with_key_result(html_data, key_html) -> str:
        """
        Function to print the keys in data
        :param data: The pydantic data object.
        :param keys: Searched keys tuple.
        """
        return html_data.replace(AnimalWebGenerator.HTML_PLACEHOLDER, key_html)

    @staticmethod
    def __get_key_results_html(title_key: str, data_list: list[dict]) -> str:
        """
        Function to print the keys in data
        :param title_key: The Title Key header.
        :param data_list: The animal keys data list.
        """
        line_list = []
        for item in data_list:
            line_list.append('<li class="cards__item">\n')
            title = ""
            sub_line_list = []
            for k, v in item.items():
                if isinstance(v, list):
                    val = str(v[0])
                else:
                    val = str(v)
                if k == title_key:
                    title = f'<div class="card__title">{val.title()}</div>\n'
                else:
                    sub_line_list.append(f"<strong>{k.title()}:</strong> {val.title()}<br/>\n")
            line_list.append(title)
            line_list.append('<p class="card__text">')
            line_list.extend(sub_line_list)
            line_list.append('</p>')
            line_list.append('</li>\n')

        res = "".join(line_list)
        return res
