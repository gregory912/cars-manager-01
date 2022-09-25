from data_loader.json import get_cars
from car.service import CarsService


def main() -> None:
    filename = r'data/cars.json'
    cars = get_cars(filename)
    CarsService(cars)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e.args[0])
