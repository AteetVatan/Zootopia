"""Data Schema Module."""
from typing import List, Dict  # typing module for specifying Explicit types.
from pydantic import BaseModel, RootModel, Field  # pydantic module for schema validation.


class Taxonomy(BaseModel):
    """Class for Json property Taxonomy."""
    kingdom: str
    phylum: str
    class_: str = Field(alias="class")  # alias class_ to handel keyword
    order: str
    family: str
    genus: str
    scientific_name: str

    class Config:
        """Class for Taxonomy default configration."""
        extra = "forbid"  # no extra fields are allowed in Taxonomy


class AnimalMetadataSchema(BaseModel):
    """Class for Animal Metadata."""
    name: str
    taxonomy: Taxonomy
    locations: List[str]
    characteristics: Dict[str, str]

    class Config:
        """Class for AnimalMetadataSchema default configration."""
        extra = "forbid"  # no extra fields are allowed in AnimalMetadataSchema


class AnimalMetadataSchemaRoot(RootModel):
    """Class for root node of Animal Metadata."""
    # The top most element should be RootModel.root. RootModel is also a subclass of BaseModel
    root: List[AnimalMetadataSchema]
