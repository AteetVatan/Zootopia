"""The Services Business logic (API calls, data fetching) package."""
from services.base_data_handler import BaseDataHandler
from services.schema_data_handler import SchemaDataHandler
from services.html_data_handler import HtmlDataHandler
from services.data_query import DataQuery
from services.animals_web_generator import AnimalWebGenerator

__all__ = ["BaseDataHandler",
           "SchemaDataHandler",
           "HtmlDataHandler",
           "DataQuery",
           "AnimalWebGenerator"]
