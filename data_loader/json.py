from car.model import Car
import json


def get_cars(filename: str) -> list[Car]:
    """
    Get data from json file and return list of Car objects
    """
    with open(filename, 'r') as json_file:
        json_data = json.load(json_file)
        return [Car(**data) for data in json_data]

