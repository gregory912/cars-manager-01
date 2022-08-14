from car.model import *
from car.service import CarsService
import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('car.service.get_cars')
    def test_sort_cars(self, mock_cars):
        """
        Test the sort_cars method for the model and price arguments
        """
        car_1 = {"model": 'MAZDA', "price": 160, "mileage": 2500, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'BMW', "price": 160, "mileage": 2500, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'AUDI', "price": 160, "mileage": 2500, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertNotEqual(cars, car_service.sort_cars("model"),
                            'Method sort_cars return wrong values for argument model.')
        self.assertEqual(cars, car_service.sort_cars("model", True),
                         'Method sort_cars return wrong values for argument model.')

        self.assertNotEqual(cars, car_service.sort_cars("color"),
                            'Method sort_cars return wrong values for argument color.')
        self.assertEqual(cars, car_service.sort_cars("color", True),
                         'Method sort_cars return wrong values for argument color.')

    @patch('car.service.get_cars')
    def test_filter_cars_by_mileage(self, mock_cars):
        """
        Test the filter_cars_by_mileage method for values 2000 and 3000
        """
        car_1 = {"model": 'MAZDA', "price": 160, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'BMW', "price": 160, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'AUDI', "price": 160, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(2, len(car_service.filter_cars_by_mileage(2000)),
                         'Method filter_cars_by_mileage return wrong values.')
        self.assertEqual(1, len(car_service.filter_cars_by_mileage(3000)),
                         'Method filter_cars_by_mileage return wrong values.')

    @patch('car.service.get_cars')
    def test_number_of_cars_with_the_same_color(self, mock_cars):
        """
        Test the number_of_cars_with_the_same_color method for WHITE and BLACK
        """
        car_1 = {"model": 'MAZDA', "price": 160, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'BMW', "price": 160, "mileage": 3000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'AUDI', "price": 160, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        car_4 = {"model": 'AUDI', "price": 160, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3), Car(**car_4)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(2, car_service.number_of_cars_with_the_same_color()[Color.BLACK],
                         'Method number_of_cars_with_the_same_color return wrong values.')
        self.assertEqual(2, car_service.number_of_cars_with_the_same_color()[Color.WHITE],
                         'Method number_of_cars_with_the_same_color return wrong values.')

    @patch('car.service.get_cars')
    def test_model_with_the_most_expensive_car(self, mock_cars):
        """
        Test model_with_the_most_expensive_car method for MAZDA, BMW, AUDI
        """
        car_1 = {"model": 'MAZDA', "price": 1000, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'MAZDA', "price": 2000, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'BMW', "price": 3000, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_4 = {"model": 'BMW', "price": 1500, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_5 = {"model": 'AUDI', "price": 1500, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        car_6 = {"model": 'AUDI', "price": 3000, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3), Car(**car_4), Car(**car_5), Car(**car_6)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(3000, car_service.model_with_the_most_expensive_car()['AUDI'].price,
                         'Method model_with_the_most_expensive_car return wrong values.')
        self.assertEqual(3000, car_service.model_with_the_most_expensive_car()['BMW'].price,
                         'Method model_with_the_most_expensive_car return wrong values.')
        self.assertEqual(2000, car_service.model_with_the_most_expensive_car()['MAZDA'].price,
                         'Method model_with_the_most_expensive_car return wrong values.')

    @patch('car.service.get_cars')
    def test_statistics_of_cars(self, mock_cars):
        """
        Test the statistics_of_cars method for the entered data
        """
        car_1 = {"model": 'MAZDA', "price": 3000, "mileage": 1000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'MAZDA', "price": 2500, "mileage": 2000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'BMW', "price": 1500, "mileage": 2500, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_4 = {"model": 'BMW', "price": 2500, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_5 = {"model": 'AUDI', "price": 3000, "mileage": 2000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        car_6 = {"model": 'AUDI', "price": 4000, "mileage": 1500, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3), Car(**car_4), Car(**car_5), Car(**car_6)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        """PRICE"""
        self.assertEqual(1500, car_service.statistics_of_cars()[0][0], 'Method statistics_of_cars return wrong values.')
        self.assertEqual(2750, car_service.statistics_of_cars()[0][1], 'Method statistics_of_cars return wrong values.')
        self.assertEqual(4000, car_service.statistics_of_cars()[0][2], 'Method statistics_of_cars return wrong values.')

        """MILEAGE"""
        self.assertEqual(1000, car_service.statistics_of_cars()[1][0], 'Method statistics_of_cars return wrong values.')
        self.assertEqual(2000, car_service.statistics_of_cars()[1][1], 'Method statistics_of_cars return wrong values.')
        self.assertEqual(3000, car_service.statistics_of_cars()[1][2], 'Method statistics_of_cars return wrong values.')

    @patch('car.service.get_cars')
    def test_the_most_expensive_cars(self, mock_cars):
        """
        Test the_most_expensive_cars method for values 2000, 1800, 2000
        """
        car_1 = {"model": 'MAZDA', "price": 2000, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'BMW', "price": 1800, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'AUDI', "price": 2000, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(2, len(car_service.the_most_expensive_cars()),
                         'Method the_most_expensive_cars return wrong values.')
        self.assertEqual(2000, car_service.the_most_expensive_cars()[0].price,
                         'Method the_most_expensive_cars return wrong values.')

    @patch('car.service.get_cars')
    def test_cars_with_sorted_list_of_components(self, mock_cars):
        """
        Test the cars_with_sorted_list_of_components method for the entered data
        """
        car_1 = {"model": 'MAZDA', "price": 2000, "mileage": 5000, "color": "WHITE", "components": [
            'ROOF RACK', 'AIR CONDITIONING', 'PANORAMIC ROOF']}
        car_2 = {"model": 'BMW', "price": 1800, "mileage": 3000, "color": "SILVER", "components": [
            'AIR CONDITIONING', 'CRUISE CONTROL', 'ABS', 'RADIO']}
        cars = [Car(**car_1), Car(**car_2)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        car_1_sorted = {"model": 'MAZDA', "price": 2000, "mileage": 5000, "color": "WHITE", "components": [
            'AIR CONDITIONING', 'PANORAMIC ROOF', 'ROOF RACK']}
        car_2_sorted = {"model": 'BMW', "price": 1800, "mileage": 3000, "color": "SILVER", "components": [
            'ABS', 'AIR CONDITIONING', 'CRUISE CONTROL', 'RADIO']}
        cars_sorted = [Car(**car_1_sorted), Car(**car_2_sorted)]

        self.assertEqual(cars_sorted, car_service.cars_with_sorted_list_of_components(),
                         'Method cars_with_sorted_list_of_components return wrong values.')

    @patch('car.service.get_cars')
    def test_component_as_key_and_value_as_cars_which_have_this_component(self, mock_cars):
        """
        Test the component_as_key_and_value_as_cars_which_have_this_component method for ABS and RADIO components
        """
        car_1 = {"model": 'MAZDA', "price": 1500, "mileage": 1000, "color": "WHITE", "components": ['ABS']}
        car_2 = {"model": 'MAZDA', "price": 2500, "mileage": 2000, "color": "WHITE", "components": ['ABS']}
        car_3 = {"model": 'BMW', "price": 1500, "mileage": 2500, "color": "SILVER", "components": ['ABS']}
        car_4 = {"model": 'BMW', "price": 2500, "mileage": 3000, "color": "SILVER", "components": ['RADIO']}
        car_5 = {"model": 'AUDI', "price": 3000, "mileage": 2000, "color": "BLACK", "components": ['RADIO']}
        car_6 = {"model": 'AUDI', "price": 4000, "mileage": 1500, "color": "BLACK", "components": ['RADIO', 'ABS']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3), Car(**car_4), Car(**car_5), Car(**car_6)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(3, len(car_service.component_as_key_and_value_as_cars_which_have_this_component()['RADIO']),
                         'Method component_as_key_and_value_as_cars_which_have_this_component return wrong values.')
        self.assertEqual(4, len(car_service.component_as_key_and_value_as_cars_which_have_this_component()['ABS']),
                         'Method component_as_key_and_value_as_cars_which_have_this_component return wrong values.')

    @patch('car.service.get_cars')
    def test_cars_with_indicated_price(self, mock_cars):
        """
        Test the cars_with_indicated_price method for 1000, 1500, 2100
        """
        car_1 = {"model": 'MAZDA', "price": 1000, "mileage": 5000, "color": "WHITE", "components": ['AIR CONDITIONING']}
        car_2 = {"model": 'BMW', "price": 1500, "mileage": 3000, "color": "SILVER", "components": ['AIR CONDITIONING']}
        car_3 = {"model": 'AUDI', "price": 2100, "mileage": 1000, "color": "BLACK", "components": ['AIR CONDITIONING']}
        cars = [Car(**car_1), Car(**car_2), Car(**car_3)]

        mock_cars.return_value = cars
        car_service = CarsService(r'../data/cars.json')

        self.assertEqual(1, len(car_service.cars_with_indicated_price(1200, 1800)),
                         'Method cars_with_indicated_price return wrong values.')
        self.assertEqual(1, len(car_service.cars_with_indicated_price(1000, 2100)),
                         'Method cars_with_indicated_price return wrong values.')
        self.assertEqual(3, len(car_service.cars_with_indicated_price(999, 2101)),
                         'Method cars_with_indicated_price return wrong values.')


if __name__ == '__main__':
    unittest.main()
