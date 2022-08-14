from car.service import CarsService


def main() -> None:
    filename = r'data/cars.json'
    cars_service = CarsService(filename)


if __name__ == '__main__':
    main()
