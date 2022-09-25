from car.validator import validate_components, validate_model, validate_price_mileage
import unittest
from decimal import Decimal


class MyTestCase(unittest.TestCase):
    def test_validate_model_correct_value(self):
        """
        Check that the validate_model method returns True for a valid item
        """
        self.assertTrue(validate_model("AUDI"), 'Method test_validate_model_correct_value return wrong values.')

    def test_validate_model_lower_letter(self):
        """
        Test that the validate_model method returns False for the lowercase element
        """
        self.assertFalse(validate_model("aAUDI"), 'Method test_validate_model_lower_letter return wrong values.')

    def test_validate_model_space(self):
        """
        Test that the validate_model method returns False for the element with a space
        """
        self.assertFalse(validate_model("AUDI "), 'Method test_validate_model_space return wrong values.')
        self.assertFalse(validate_model(" AUDI"), 'Method test_validate_model_space return wrong values.')

    def test_validate_model_digit(self):
        """
        Test that the validate_model method returns False for the item with numbers
        """
        self.assertFalse(validate_model("AUDI1"), 'Method test_validate_model_digit return wrong values.')

    def test_validate_model_empty_string(self):
        """
        Test that the validate_model method returns False for the empty string
        """
        self.assertFalse(validate_model(""), 'Method test_validate_model_empty_string return wrong values.')

    def test_validate_model_empty_space(self):
        """
        Test that the validate_model method returns False for a blank space
        """
        self.assertFalse(validate_model(" "), 'Method test_validate_model_empty_space return wrong values.')

    def test_validate_price_mileage_correct_values(self):
        """
        Test that the validate_price_mileage method returns True for valid values
        """
        self.assertTrue(validate_price_mileage(0),
                        'Method test_validate_price_mileage_correct_values return wrong values.')
        self.assertTrue(validate_price_mileage(100),
                        'Method test_validate_price_mileage_correct_values return wrong values.')

    def test_validate_price_mileage_correct_values_decimal(self):
        """
        Test that the validate_price_mileage method returns True for valid values
        """
        self.assertTrue(validate_price_mileage(Decimal(100)),
                        'Method test_validate_price_mileage_correct_values_decimal return wrong values.')

    def test_validate_price_mileage_wrong_value(self):
        """
        Test that the validate_price_mileage method returns False for negative values
        """
        self.assertFalse(validate_price_mileage(-100),
                         'Method test_validate_price_mileage_wrong_value return wrong values.')

    def test_validate_price_mileage_wrong_value_decimal(self):
        """
        Test that the validate_price_mileage method returns False for negative values
        """
        self.assertFalse(validate_price_mileage(Decimal(-100)),
                         'Method test_validate_price_mileage_wrong_value_decimal return wrong values.')

    def test_validate_components_single_word_component(self):
        """
        Test that the validate_components method returns True for valid values
        """
        self.assertTrue(validate_components("ABS"),
                        'Method test_validate_components_single_word_component return wrong values.')

    def test_validate_components_many_words_component(self):
        """
        Test that the validate_components method returns True for valid values
        """
        self.assertTrue(validate_components("ROOF RACK"),
                        'Method test_validate_components_many_words_component return wrong values.')
        self.assertTrue(validate_components("ROOF   RACK"),
                        'Method test_validate_components_many_words_component return wrong values.')

    def test_validate_components_lower_letter(self):
        """
        Test that the validate_components method returns False for lowercase elements
        """
        self.assertFalse(validate_components("aABS"),
                         'Method test_validate_components_lower_letter return wrong values.')

    def test_validate_components_space(self):
        """
        Test that the validate_components method returns False for items with a space
        """
        self.assertFalse(validate_components(" ABS"), 'Method test_validate_components_space return wrong values.')
        self.assertFalse(validate_components("ABS "), 'Method test_validate_components_space return wrong values.')
        self.assertFalse(validate_components(" ABS "), 'Method test_validate_components_space return wrong values.')

    def test_validate_components_digits(self):
        """
        Test that the validate_components method returns False for items with numbers
        """
        self.assertFalse(validate_components("ABS1"), 'Method test_validate_components_digits return wrong values.')
        self.assertFalse(validate_components("ABS1"), 'Method test_validate_components_digits return wrong values.')

    def test_validate_components_empty_string(self):
        """
        Test that the validate_components method returns False for an empty string
        """
        self.assertFalse(validate_components(""), 'Method test_validate_components_empty_string return wrong values.')

    def test_validate_components_empty_space(self):
        """
        Test that the validate_components method returns False for a blank space
        """
        self.assertFalse(validate_components(" "), 'Method test_validate_components_empty_space return wrong values.')
