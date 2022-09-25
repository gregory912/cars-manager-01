from .validator import validate_car
from .enums import Color
from dataclasses import dataclass
from decimal import Decimal
from typing import Any


@dataclass
class Car:
    model: str
    price: Decimal
    mileage: int
    color: Color
    components: list[str]

    @classmethod
    def get_model(cls, data: [str, Any]) -> 'Car':
        """Return properly formatted data"""
        return Car(
            data['model'],
            Decimal(str(data['price'])),
            data['mileage'],
            Color.value_of(data['color']) if not isinstance(data['color'], Color) else data['color'],
            data['components'])

    def __post_init__(self):
        """
        Check that the elements entered into the class are in the correct format
        """
        validate_car(self)

    def has_mileage_greater_than(self, expected_mileage: int):
        """
        Check if the expected mileage is greater than the entered mileage in the object
        """
        return self.mileage > expected_mileage

    def with_sorted_components(self) -> 'Car':
        """
        Return the Car object in which the components are sorted
        """
        return Car(self.model, self.price, self.mileage, self.color, sorted(self.components))

    def has_component(self, expected_component: str) -> bool:
        """
        Check if the component is included in the list of the given object
        """
        return expected_component in self.components

    def has_price_between(self, min_price: Decimal, max_price: Decimal) -> bool:
        """
        Check if the price of a given car is within the entered range
        """
        return min_price <= self.price <= max_price

