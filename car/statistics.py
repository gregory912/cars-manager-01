from statistics import mean
from decimal import Decimal


class CarStatistics:

    def __init__(self, values: list[int | Decimal]):
        self.values = values

    def min_value(self):
        """
        The function returns the minimum value from the price list
        """
        return min(self.values)

    def average_value(self):
        """
        The function returns the average value from the price list
        """
        return round(mean(self.values), 2)

    def max_value(self):
        """
        The function returns the maximum value from the price list
        """
        return max(self.values)

    @property
    def get_min_avg_max(self) -> tuple:
        """Return all stats"""
        return self.min_value(), self.average_value(), self.max_value()
