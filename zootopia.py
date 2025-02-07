"""THe Main Zootopia Module"""
from typing import Type
from data.schema_data_handler import SchemaDataHandler
from data.animal_metadata_schema import AnimalMetadataSchemaRoot
from web.animals_web_generator import AnimalWebGenerator


def init_zootopia():
    """Main function for Zootopia application."""
    sdh = SchemaDataHandler("animals_data.json", "data", AnimalMetadataSchemaRoot)  # The schema class instance.
    data = sdh.data  # Json data from file cast to the AnimalMetadataSchemaRoot class
    awg = AnimalWebGenerator("animals_template.html", "") # AnimalWebGenerator reads data from animals_template.html.
    search_keys = ("name", "diet", "locations", "type")  # The Keys to be searched and display in HTML.
    awg.display_key_info_in_html(data, search_keys, search_keys[0], "animals.html") # All searched keys are written to a file animals.html


if __name__ == "__main__":
    init_zootopia()
