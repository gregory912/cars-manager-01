import json
from car.model import Car


def get_cars(filename: str) -> list:
    """
    Get data from json file and return list of Car objects
    """
    with open(filename) as json_file:
        json_data = json.load(json_file)
        return [Car.get_model(data) for data in json_data]
