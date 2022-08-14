from car.validator import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_validate_model(self):
        """
        Test if the validate_model method validates the entered data correctly
        """
        self.assertEqual(True, validate_model("AUDI"), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model("aAUDI"), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model("AUDI "), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model(" AUDI"), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model("AUDI1"), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model(""), 'Method validate_model return wrong values.')
        self.assertNotEqual(True, validate_model(" "), 'Method validate_model return wrong values.')

    def test_validate_price_mileage(self):
        """
        Test if the validate_price_mileage method correctly validates the entered data
        """
        self.assertEqual(True, validate_price_mileage(0), 'Method validate_price_mileage return wrong values.')
        self.assertEqual(True, validate_price_mileage(100), 'Method validate_price_mileage return wrong values.')
        self.assertNotEqual(True, validate_price_mileage(-100), 'Method validate_price_mileage return wrong values.')
        self.assertEqual(True, validate_price_mileage(Decimal(100)),
                         'Method validate_price_mileage return wrong values.')
        self.assertNotEqual(True, validate_price_mileage(Decimal(-100)),
                            'Method validate_price_mileage return wrong values.')

    def test_validate_components(self):
        """
        Test if the validate components method validates the entered data correctly
        """
        self.assertEqual(True, validate_components("ABS"), 'Method validate_components return wrong values.')
        self.assertEqual(True, validate_components("ROOF RACK"), 'Method validate_components return wrong values.')
        self.assertEqual(True, validate_components("ROOF   RACK"), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components("aABS"), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components(" ABS"), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components("ABS "), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components(" ABS "), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components("ABS1"), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components("ABS1"), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components(""), 'Method validate_components return wrong values.')
        self.assertNotEqual(True, validate_components(" "), 'Method validate_components return wrong values.')
