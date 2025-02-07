"""THe Main Zootopia Module"""
from data.schema_data_handler import SchemaDataHandler
from data.animal_metadata_schema import AnimalMetadataSchemaRoot
from web.animals_web_generator import AnimalWebGenerator


def init_zootopia():
    """Main function for Zootopia application."""
    # The schema class instance.
    sdh = SchemaDataHandler("animals_data.json", "data", AnimalMetadataSchemaRoot)
    # Json data from file cast to the AnimalMetadataSchemaRoot class
    data = sdh.data
    # AnimalWebGenerator reads data from animals_template.html.
    awg = AnimalWebGenerator("animals_template.html", "")
    # The Keys to be searched and display in HTML.
    search_keys = ("name", "diet", "locations", "type", "kingdom", "slogan", "diet",
                   "average_litter_size")
    # All searched keys are written to a file animals.html
    awg.display_key_info_in_html(data, search_keys, search_keys[0],
                                 "animals.html")


if __name__ == "__main__":
    init_zootopia()
