import unittest
from car.service import *
from tests.test_data.data import CAR_TEST_MODEL


class MyTestCase(unittest.TestCase):

    car = CAR_TEST_MODEL

    def test_data_types_model(self):
        """
        Test if the model field is properly defined
        """
        self.assertIsInstance(self.car.model, str, 'Method test_data_types_model return wrong values.')

    def test_data_types_price(self):
        """
        Test if the price field is properly defined
        """
        self.assertIsInstance(self.car.price, Decimal, 'Method test_data_types_price return wrong values.')

    def test_data_types_mileage(self):
        """
        Test if the mileage field is properly defined
        """
        self.assertIsInstance(self.car.mileage, int, 'Method test_data_types_mileage return wrong values.')

    def test_data_types_color(self):
        """
        Test if the color field is properly defined
        """
        self.assertIsInstance(self.car.color, Color, 'Method test_data_types_color return wrong values.')

    def test_data_types_components(self):
        """
        Test if the component field is properly defined
        """
        self.assertIsInstance(self.car.components, list, 'Method test_data_types_components return wrong values.')

    def test_has_mileage_greater_than_values_in_limit(self):
        """
        Test if the method test_has_mileage_greater_than_values_over_limit returns True for numbers in the range
        """
        self.assertTrue(self.car.has_mileage_greater_than(2000),
                        'Method test_has_mileage_greater_than_values_in_limit return wrong values.')
        self.assertTrue(self.car.has_mileage_greater_than(2499),
                        'Method test_has_mileage_greater_than_values_in_limit return wrong values.')

    def test_has_mileage_greater_than_values_over_limit(self):
        """
        Test if the method test_has_mileage_greater_than_values_over_limit returns False for numbers out of range
        """
        self.assertFalse(self.car.has_mileage_greater_than(2500),
                         'Method test_has_mileage_greater_than_values_over_limit return wrong values.')
        self.assertFalse(self.car.has_mileage_greater_than(3000),
                         'Method test_has_mileage_greater_than_values_over_limit return wrong values.')

    def test_with_sorted_components(self):
        """
        Check if the with_sorted_components method sorts items properly
        """
        car = self.car.with_sorted_components()
        self.assertEqual(car.components, ["ABS", "BLUETOOTH", "CRUISE CONTROL", "RADIO"],
                         'Method test_with_sorted_components return wrong values.')
        self.assertEqual(len(car.components), 4, 'Method test_with_sorted_components return wrong values.')

    def test_has_component_with_components(self):
        """
        Test if the test_has_component_without components method
        returns True for the components that the object has
        """
        self.assertTrue(self.car.has_component("RADIO"),
                        'Method test_has_component_with_components return wrong values.')
        self.assertTrue(self.car.has_component("ABS"),
                        'Method test_has_component_with_components return wrong values.')

    def test_has_component_without_components(self):
        """
        Test if the test_has_component_without_components method
        returns False for components which the object does not have
        """
        self.assertFalse(self.car.has_component("ALLOY WHEELS"),
                         'Method test_has_component_without_components return wrong values.')
        self.assertFalse(self.car.has_component("ANDROID AUTO"),
                         'Method test_has_component_without_components return wrong values.')

    def test_has_price_between_in_limit(self):
        """
        Test that the has_price_between method returns True for valid values
        """
        self.assertTrue(self.car.has_price_between(150, 170),
                        'Method test_has_price_between_in_limit return wrong values.')
        self.assertTrue(self.car.has_price_between(160, 162),
                        'Method test_has_price_between_in_limit return wrong values.')

    def test_has_price_between_over_limit(self):
        """
        Test that has_price_between returns False for out of range values
        """
        self.assertFalse(self.car.has_price_between(161, 162),
                         'Method test_has_price_between_over_limit return wrong values.')
        self.assertFalse(self.car.has_price_between(180, 183),
                         'Method test_has_price_between_over_limit return wrong values.')


if __name__ == '__main__':
    unittest.main()
