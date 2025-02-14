"""THe Main Zootopia Module"""
from data.schema_data_handler import SchemaDataHandler
from data.file_handler import FileHandler
from data.animal_metadata_schema import AnimalMetadataSchemaRoot
from web.animals_web_generator import AnimalWebGenerator
import config


def init_zootopia():
    """Main function for Zootopia application."""

    # File Handeling
    # fh = FileHandler(("animals_data.json", "data"))

    # The schema class instance.

    sdh = SchemaDataHandler(AnimalMetadataSchemaRoot,
                            (config.ANIMALS_JSON_DATA_FILE, config.ANIMALS_JSON_DATA_FILE_DIR),
                            config.LOAD_DATA_FROM_API)
    # Json data from file cast to the AnimalMetadataSchemaRoot class
    data = sdh.data
    # AnimalWebGenerator reads data from animals_template.html.
    awg = AnimalWebGenerator(config.ANIMALS_HTML_TEMPLATE, config.ANIMALS_HTML_TEMPLATE_DIR)
    # The Keys to be searched and display in HTML.
    search_keys = ("name", "diet", "locations", "type", "kingdom", "slogan", "diet",
                   "average_litter_size")
    # All searched keys are written to a file animals.html
    awg.display_key_info_in_html(data, search_keys, search_keys[0],
                                 config.ANIMALS_HTML_FILE)


if __name__ == "__main__":
    init_zootopia()
