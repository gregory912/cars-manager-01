from data_loader.json import *
from .statistics import CarStatistics
from car.enums import *
from operator import attrgetter
from itertools import groupby, takewhile
from decimal import Decimal


class CarsService:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    def __str__(self):
        """
        Enter all car data into the appropriate format for display
        """
        cars = ""
        for item in self.cars:
            cars += f"""
                    Car model: {item.model}
                    Price: {item.price}
                    Mileage: {item.mileage}
                    Color: {item.color.name}
                    Components: {', '.join(item.components)}
                    """
        return cars

    def sort_cars(self, sort_type: Enum, descending: bool = False) -> list['Car']:
        """
        A method that returns a new collection of Car elements
        sorted by the specified criterion method argument.
        The method should be able to sort by model name, color, price and mileage.
        Additionally, you should define whether sorting is to be done in descending or ascending way.
        """
        return sorted(self.cars, key=attrgetter(sort_type.name.lower()), reverse=descending)

    def filter_cars_by_mileage(self, limit_mileage: int) -> list['Car']:
        """
        The method returns a collection of Car type elements that
        have a mileage greater than the element given as an argument of the method.
        """
        if limit_mileage < 0:
            raise ValueError('The mileage entered is invalid')
        return [car for car in self.cars if car.has_mileage_greater_than(limit_mileage)]

    def get_number_of_cars_with_the_same_color(self) -> dict['Color', int]:
        """
        The method returns a dict whose key is a color,
        and the element is the number of cars that have that color.
        The dict should be sorted in descending order of values.
        """
        color_dict = {}
        cars = self.sort_cars(SortType.COLOR)
        group_obj = groupby(cars, key=lambda x: x.color)
        for key, value in group_obj:
            color_dict[key] = len(list(value))

        return {k: v for k, v in sorted(color_dict.items(), key=lambda item: item[1], reverse=True)}

    def get_model_with_the_most_expensive_car(self) -> dict[str, 'Car']:
        """
        The method returns a dict whose key is the name of the car model,
        and the element of an object of class Car, which represents
        the most expensive car with this model name.
        The dict should be sorted by keys in descending order.
        """
        model_dict = {}
        cars = self.sort_cars(SortType.MODEL)
        group_obj = groupby(cars, key=lambda x: x.model)

        for key, value in group_obj:
            model_dict[key] = sorted(list(value), key=lambda x: x.price, reverse=True)[0]

        return model_dict

    def get_statistics_of_cars(self) -> tuple[tuple[float], tuple[float]]:
        """
        The method lists the car statistics in the list.
        The statistics should include the average element,
        the lowest element, and the highest element for
        the fields describing the price and mileage of cars.
        """
        prices = CarStatistics(self.get_list_of_values('price', self.cars))
        mileages = CarStatistics(self.get_list_of_values('mileage', self.cars))
        return prices.get_min_avg_max, mileages.get_min_avg_max

    def get_the_most_expensive_cars(self) -> list[Car]:
        """
        The method returns the car with the highest price.
        In the event that more than one car has the highest price,
        the collection of these cars should be returned.
        """
        cars = self.sort_cars(SortType.PRICE, True)
        cars_prices = self.get_list_of_values('price', cars)
        result = list(takewhile(lambda x: x == cars_prices[0], cars_prices))
        return cars[:len(result)]

    def get_cars_with_sorted_list_of_components(self) -> list[Car]:
        """
        The method returns a collection of cars in which
        each car has an alphabetically sorted collection of components.
        """
        return [x.with_sorted_components() for x in self.cars]

    def get_components_with_cars(self) -> dict[str, list]:
        """
        The method returns a map whose key is the name of the component,
        and the element is the collection of cars that have this component.
        The pairs in the map should be sorted in descending order by
        the number of elements in the collection representing the element of the pair.
        """
        component_dict = {}
        set_components = set()
        [[set_components.add(component) for component in item.components] for item in self.cars]

        for component in set_components:
            component_dict[component] = [car for car in self.cars if car.has_component(component)]

        component_dict = dict(sorted(component_dict.items(), key=lambda y: len(y[1]), reverse=True))
        return component_dict

    def get_cars_with_price_between(self, min_price: Decimal, max_price: Decimal) -> list[Car]:
        """
        The method returns a collection of cars whose price is in the price range <a, b>.
        The values of a and b are passed as an argument to the method.
        The collection should be sorted alphabetically by car name.
        """
        if min_price < 0 or min_price > max_price:
            raise ValueError('The entered range is not correct')
        cars = [x for x in self.cars if x.has_price_between(min_price, max_price)]
        return sorted(cars, key=attrgetter('model'))

    @staticmethod
    def get_list_of_values(element: str, cars: list[Car]) -> list[int]:
        """
        Get a list with values for the selected item
        """
        return [[b for a, b in x.__dict__.items() if a == element][0] for x in cars]
