from .validator import *
from .enums import *
from dataclasses import dataclass


@dataclass
class Car:
    model: str
    price: Decimal
    mileage: int
    color: Color
    components: list[str]

    def __post_init__(self):
        """
        Check that the elements entered into the class are in the correct format
        """
        if not validate_model(self.model):
            raise ValueError("The entered model is invalid.")
        if not validate_price_mileage(self.price):
            raise ValueError("The entered price is incorrect.")
        if not validate_price_mileage(self.mileage):
            raise ValueError("The entered mileage is incorrect.")
        self.color = Color.value_of(self.color) if not isinstance(self.color, Color) else self.color
        if not validate_components(" ".join(self.components)):
            raise ValueError("The entered components are invalid.")
