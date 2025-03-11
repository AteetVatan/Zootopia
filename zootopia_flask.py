"""THe Main Zootopia Flask Module"""
import os
import sys
from typing import List, Dict

from flask import Flask, request, render_template

from models.animal_metadata_schema_model import AnimalMetadataSchemaRoot
from services.schema_data_handler import SchemaDataHandler
from services.animals_web_generator import AnimalWebGenerator
from constants import constants

app = Flask(__name__)  # initializes a Flask web application.


def zootopia(search_item="") -> List[Dict]:
    """Main function for Zootopia application."""
    try:
        if search_item:
            sdh = SchemaDataHandler(AnimalMetadataSchemaRoot, search_item)
        else:
            sdh = SchemaDataHandler(AnimalMetadataSchemaRoot)
        # JSON data from a file cast to the AnimalMetadataSchemaRoot class
        data = sdh.data
        # AnimalWebGenerator reads data from animals_template.html.
        awg = AnimalWebGenerator()
        # All searched keys are written to a file animals.html
        awg.set_query_data(data)
        return awg.query_data
    except Exception as e:
        print(f"Error {constants.APP_NAME}: {str(e)}")
        sys.exit(1)


@app.route('/')
def welcome():
    """The main welcome Method."""
    return render_template('home_template.html',
                           welcome_msg=constants.WELCOME_MESSAGE,
                           user_question=constants.USER_INPUT)


@app.route('/animal-info', methods=['GET'])
def animal_info():
    """Flask method to get animal info."""
    animal_name = request.args.get('name', '').strip()
    animal_data = zootopia(animal_name)
    return render_template('animals_template_flask.html', animal_data=animal_data)


@app.route('/debug-template')
def debug_template():
    """Method to debug"""
    template_path = os.path.join(os.getcwd(), "templates", "animal_template_flask.html")
    return f"Looking for template at: {template_path}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)  # starts a small web server.
