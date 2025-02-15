"""THe Main Zootopia Module"""
import sys

from models.animal_metadata_schema_model import AnimalMetadataSchemaRoot
from services.schema_data_handler import SchemaDataHandler
from services.animals_web_generator import AnimalWebGenerator


def zootopia():
    """Main function for Zootopia application."""
    try:
        sdh = SchemaDataHandler(AnimalMetadataSchemaRoot)
        # Json data from file cast to the AnimalMetadataSchemaRoot class
        data = sdh.data
        # AnimalWebGenerator reads data from animals_template.html.
        awg = AnimalWebGenerator()
        # All searched keys are written to a file animals.html
        awg.display_key_info_in_html(data)
    except Exception as e:# c0mmon place to cat
        print(f"Error Zootopia: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    zootopia()
