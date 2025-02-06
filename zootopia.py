"""THe Main Zootopia Module"""
from data.data_handler import DataHandler
from data.animal_metadata_schema import AnimalMetadataSchemaRoot


def init_zootopia():
    DataHandler.load_data(AnimalMetadataSchemaRoot)
    animal_obj = DataHandler.get_data()
    print("Done")
    print(animal_obj.__dict__)


if __name__ == "__main__":
    init_zootopia()
