"""THe Main Zootopia Module"""
import sys

import config
from models.animal_metadata_schema_model import AnimalMetadataSchemaRoot
from services.schema_data_handler import SchemaDataHandler
from services.animals_web_generator import AnimalWebGenerator
from constants import constants


def zootopia():
    """Main function for Zootopia application."""
    try:
        search_item = None
        if config.AllOW_USER_INPUT:
            search_item = get_user_input()
            sdh = SchemaDataHandler(AnimalMetadataSchemaRoot, search_item)
        else:
            sdh = SchemaDataHandler(AnimalMetadataSchemaRoot)
        # Json data from file cast to the AnimalMetadataSchemaRoot class
        data = sdh.data
        # AnimalWebGenerator reads data from animals_template.html.
        awg = AnimalWebGenerator()
        # All searched keys are written to a file animals.html
        success = awg.display_key_info_in_html(data, search_item=search_item)
        if success:
            print(constants.APP_SUCCESS.format(file_name=config.ANIMALS_HTML_FILE))
        else:
            print(constants.APP_NO_RESULT.format(file_name=config.ANIMALS_HTML_FILE))
    except Exception as e:  # c0mmon place to cat
        print(f"Error {constants.APP_NAME}: {str(e)}")
        sys.exit(1)


def get_user_input() -> str:
    """Function to get User Input."""
    while True:
        try:
            usr_input = input(constants.USER_INPUT).strip().lower()
            if not usr_input:
                raise ValueError(constants.USER_INPUT_ERROR)
            return usr_input
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    zootopia()
