from car.model import Car
from data_loader.json import get_cars
from operator import attrgetter
from itertools import groupby, takewhile
from statistics import mean
import re


class CarsService:
    def __init__(self, filename: str):
        self.cars = get_cars(filename)

        # print(self.sort_cars("color", True))
        # print(self.filter_cars_by_mileage(3000))
        # print(self.number_of_cars_with_the_same_color())
        # print(self.model_with_the_most_expensive_car())
        # print(self.statistics_of_cars())
        # print(self.the_most_expensive_cars())
        # print(self.cars_with_sorted_list_of_components())
        # print(self.component_as_key_and_value_as_cars_which_have_this_component())
        # print(self.cars_with_indicated_price(1000, 6000))

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

    def sort_cars(self, sort_type: str, descending: bool = False) -> list['Car']:
        """
        A method that returns a new collection of Car elements
        sorted by the specified criterion method argument.
        The method should be able to sort by model name, color, price and mileage.
        Additionally, you should define whether sorting is to be done in descending or ascending way.
        """
        cars = self.cars.copy()
        cars.sort(key=attrgetter(sort_type), reverse=descending)
        return cars

    def filter_cars_by_mileage(self, max_mileage: int) -> list['Car']:
        """
        The method returns a collection of Car type elements that
        have a mileage greater than the value given as an argument of the method.
        """
        cars = self.cars.copy()
        return list(filter(lambda x: x.mileage > max_mileage, cars))

    def number_of_cars_with_the_same_color(self) -> dict:
        """
        The method returns a dict whose key is a color,
        and the value is the number of cars that have that color.
        The dict should be sorted in descending order of values.
        """
        color_dict = {}
        cars = self.sort_cars('color')
        group_obj = groupby(cars, key=lambda x: x.color)
        for key, value in group_obj:
            color_dict[key] = len(list(value))

        return {k: v for k, v in sorted(color_dict.items(), key=lambda item: item[1], reverse=True)}

    def model_with_the_most_expensive_car(self) -> dict:
        """
        The method returns a dict whose key is the name of the car model,
        and the value of an object of class Car, which represents
        the most expensive car with this model name.
        The dict should be sorted by keys in descending order.
        """
        model_dict = {}
        cars = self.sort_cars('model')
        group_obj = groupby(cars, key=lambda x: x.model)
        for key, value in group_obj:
            model_dict[key] = sorted(list(value), key=lambda x: x.price, reverse=True)[0]
        return model_dict

    def statistics_of_cars(self) -> tuple:
        """
        The method lists the car statistics in the list.
        The statistics should include the average value,
        the lowest value, and the highest value for
        the fields describing the price and mileage of cars.
        """

        def get_statistics(values: list[int]) -> tuple:
            return min(values), round(mean(values), 2), max(values)

        return get_statistics(self.get_list_of_values('price', self.cars)), \
            get_statistics(self.get_list_of_values('mileage', self.cars))

    def the_most_expensive_cars(self) -> list[Car]:
        """
        The method returns the car with the highest price.
        In the event that more than one car has the highest price,
        the collection of these cars should be returned.
        """
        cars = self.sort_cars('price', True)
        cars_prices = self.get_list_of_values('price', cars)
        result = list(takewhile(lambda x: x == cars_prices[0], cars_prices))
        return cars[:len(result)]

    def cars_with_sorted_list_of_components(self) -> list[Car]:
        """
        The method returns a collection of cars in which
        each car has an alphabetically sorted collection of components.
        """
        cars_dict = [x.__dict__ for x in self.cars]
        sorted_components = [sorted(x['components'], key=lambda y: y) for x in cars_dict]
        for counter, item in enumerate(cars_dict):
            cars_dict[counter]['components'] = sorted_components[counter]
        return [Car(**i) for i in cars_dict]

    def component_as_key_and_value_as_cars_which_have_this_component(self) -> dict:
        """
        The method returns a map whose key is the name of the component,
        and the value is the collection of cars that have this component.
        The pairs in the map should be sorted in descending order by
        the number of elements in the collection representing the value of the pair.
        """
        component_dict = {}
        components = [item.components for item in self.cars]
        set_components = set(re.findall(r'[A-Z ]+', str(components)))
        for component in set_components:
            component_dict[component] = [item for item in self.cars if component in item.components]
        component_dict = sorted(component_dict.items(), key=lambda y: len(y[1]), reverse=True)
        return dict(component_dict)

    def cars_with_indicated_price(self, min_price: int, max_price: int) -> list[Car]:
        """
        The method returns a collection of cars whose price is in the price range <a, b>.
        The values of a and b are passed as an argument to the method.
        The collection should be sorted alphabetically by car name.
        """
        cars = self.cars.copy()
        cars = [x for x in cars if min_price < x.price < max_price]
        cars.sort(key=attrgetter('model'))
        return cars

    @staticmethod
    def get_list_of_values(name: str, list_of_cars: list[Car]) -> list[int]:
        """
        Get a list with values for the selected item
        """
        return [[b for a, b in x.__dict__.items() if a == name][0] for x in list_of_cars]
