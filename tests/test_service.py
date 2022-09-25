from car.service import *
import unittest
from tests.test_data.data import *


class MyTestCase(unittest.TestCase):

    mazda = MAZDA
    mazda_1 = MAZDA_1
    bmw = BMW
    bmw_1 = BMW_1
    audi = AUDI
    audi_1 = AUDI_1
    peugeot = PEUGEOT
    renault = RENAULT
    ford = FORD
    ford_1 = FORD_1
    seat = SEAT
    seat_1 = SEAT_1

    def test_sort_cars_by_model(self):
        """
        Test the sort_cars method by the model
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertNotEqual(car_service.cars, car_service.sort_cars(SortType.MODEL),
                            'Method test_sort_cars_by_model return wrong values.')

    def test_sort_cars_by_model_descending(self):
        """
        Test the sort_cars method by the model descending
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertEqual(car_service.cars, car_service.sort_cars(SortType.MODEL, True),
                         'Method test_sort_cars_by_model_descending return wrong values.')

    def test_sort_cars_by_color(self):
        """
        Test the sort_cars method by the color
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertNotEqual(car_service.cars, car_service.sort_cars(SortType.COLOR),
                            'Method test_sort_cars_by_color return wrong values.')

    def test_sort_cars_by_color_descending(self):
        """
        Test the sort_cars method by the color descending
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertEqual(car_service.cars, car_service.sort_cars(SortType.COLOR, True),
                         'Method test_sort_cars_by_color_descending return wrong values.')

    def test_filter_cars_by_mileage_2000(self):
        """
        Test the filter_cars_by_mileage method for value 2000
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertEqual(2, len(car_service.filter_cars_by_mileage(2000)),
                         'Method test_filter_cars_by_mileage_2000 return wrong values.')

    def test_filter_cars_by_mileage_3000(self):
        """
        Test the filter_cars_by_mileage method for value 3000
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi])

        self.assertEqual(1, len(car_service.filter_cars_by_mileage(3000)),
                         'Method test_filter_cars_by_mileage_3000 return wrong values.')

    def test_get_number_of_cars_with_the_same_color_silver(self):
        """
        Test the get_number_of_cars_with_the_same_color method for SILVER color
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi, self.peugeot, self.renault])

        self.assertEqual(2, car_service.get_number_of_cars_with_the_same_color()[Color.SILVER],
                         'Method test_get_number_of_cars_with_the_same_color_silver return wrong values.')

    def test_get_number_of_cars_with_the_same_color_white(self):
        """
        Test the get_number_of_cars_with_the_same_color method for WHITE color
        """
        car_service = CarsService([self.mazda, self.bmw, self.audi, self.peugeot, self.renault])

        self.assertEqual(2, car_service.get_number_of_cars_with_the_same_color()[Color.WHITE],
                         'Method test_get_number_of_cars_with_the_same_color_white return wrong values.')

    def test_get_model_with_the_most_expensive_car_audi(self):
        """
        Test get_model_with_the_most_expensive_car_audi method for MAZDA, BMW, AUDI
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.bmw_1, self.audi, self.audi_1])

        self.assertEqual(250, car_service.get_model_with_the_most_expensive_car()['AUDI'].price,
                         'Method test_get_model_with_the_most_expensive_car_audi return wrong values.')

    def test_get_model_with_the_most_expensive_car_bmw(self):
        """
        Test get_model_with_the_most_expensive_car_audi method for MAZDA, BMW, AUDI
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.bmw_1, self.audi, self.audi_1])

        self.assertEqual(400, car_service.get_model_with_the_most_expensive_car()['BMW'].price,
                         'Method test_get_model_with_the_most_expensive_car_bmw return wrong values.')

    def test_get_model_with_the_most_expensive_car_mazda(self):
        """
        Test get_model_with_the_most_expensive_car_audi method for MAZDA, BMW, AUDI
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.bmw_1, self.audi, self.audi_1])

        self.assertEqual(300, car_service.get_model_with_the_most_expensive_car()['MAZDA'].price,
                         'Method test_get_model_with_the_most_expensive_car_mazda return wrong values.')

    def test_get_statistics_of_cars_for_prices(self):
        """
        Test the get_statistics_of_cars_for_prices method for prices
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.bmw_1, self.audi])

        self.assertEqual(160, car_service.get_statistics_of_cars()[0][0],
                         'Method test_get_statistics_of_cars_for_prices return wrong values.')
        self.assertEqual(236, car_service.get_statistics_of_cars()[0][1],
                         'Method test_get_statistics_of_cars_for_prices return wrong values.')
        self.assertEqual(400, car_service.get_statistics_of_cars()[0][2],
                         'Method test_get_statistics_of_cars_for_prices return wrong values.')

    def test_get_statistics_of_cars_for_mileages(self):
        """
        Test the get_statistics_of_cars_for_prices method for mileages
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.bmw_1, self.audi])

        self.assertEqual(1000, car_service.get_statistics_of_cars()[1][0],
                         'Method test_get_statistics_of_cars_for_mileages return wrong values.')
        self.assertEqual(3400, car_service.get_statistics_of_cars()[1][1],
                         'Method test_get_statistics_of_cars_for_mileages return wrong values.')
        self.assertEqual(5000, car_service.get_statistics_of_cars()[1][2],
                         'Method test_get_statistics_of_cars_for_mileages return wrong values.')

    def test_get_the_most_expensive_cars(self):
        """
        Test get_the_most_expensive_cars method
        """
        car_service = CarsService([self.mazda, self.mazda_1, self.bmw, self.audi, self.peugeot])

        self.assertEqual(2, len(car_service.get_the_most_expensive_cars()),
                         'Method test_get_the_most_expensive_cars return wrong values.')
        self.assertEqual(300, car_service.get_the_most_expensive_cars()[0].price,
                         'Method test_get_the_most_expensive_cars return wrong values.')

    def test_get_cars_with_sorted_list_of_components(self):
        """
        Test the get_cars_with_sorted_list_of_components method for the entered data
        """
        car_service = CarsService([self.ford, self.seat])
        cars_sorted = CarsService([self.ford_1, self.seat_1])

        self.assertEqual(cars_sorted.cars, car_service.get_cars_with_sorted_list_of_components(),
                         'Method test_get_cars_with_sorted_list_of_components return wrong values.')

    def test_get_components_with_cars_for_radio(self):
        """
        Test the get_components_with_cars method for RADIO component
        """
        car_service = CarsService([self.mazda, self.bmw, self.bmw_1, self.audi, self.audi_1, self.peugeot])

        self.assertEqual(4, len(car_service.get_components_with_cars()['RADIO']),
                         'Method test_get_components_with_cars_for_radio return wrong values.')

    def test_get_components_with_cars_for_abs(self):
        """
        Test the get_components_with_cars method for ABS component
        """
        car_service = CarsService([self.mazda, self.bmw, self.bmw_1, self.audi, self.audi_1, self.peugeot])
        self.assertEqual(3, len(car_service.get_components_with_cars()['ABS']),
                         'Method test_get_components_with_cars_for_abs return wrong values.')

    def test_get_cars_with_price_between_200_400(self):
        """
        Test the get_cars_with_price_between method for prices between 200 - 400
        """
        car_service = CarsService([self.mazda, self.bmw, self.bmw_1, self.audi, self.audi_1, self.peugeot])

        self.assertEqual(3, len(car_service.get_cars_with_price_between(200, 400)),
                         'Method test_get_cars_with_price_between_200_400 return wrong values.')

    def test_get_cars_with_price_between_300_400(self):
        """
        Test the get_cars_with_price_between method for prices between 300 - 400
        """
        car_service = CarsService([self.mazda, self.bmw, self.bmw_1, self.audi, self.audi_1, self.peugeot])

        self.assertEqual(2, len(car_service.get_cars_with_price_between(300, 400)),
                         'Method test_get_cars_with_price_between_300_400 return wrong values.')

    def test_get_list_of_values(self):
        """
        Test the get_list_of_values method for prices
        """
        car_service = CarsService([self.mazda, self.bmw, self.bmw_1, self.audi, self.audi_1, self.peugeot])
        self.assertEqual([160, 160, 400, 160, 250, 300], car_service.get_list_of_values('price', car_service.cars),
                         'Method test_get_list_of_values return wrong values.')


if __name__ == '__main__':
    unittest.main()
