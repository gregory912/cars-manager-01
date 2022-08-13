from dataclasses import dataclass
from decimal import Decimal
from .enums import Color


@dataclass
class Car:
    model: str
    price: Decimal
    mileage: int
    color: Color
    components: list[str]
