from enum import Enum, IntEnum


class Color(IntEnum):
    BLACK = 1
    SILVER = 2
    WHITE = 3

    @classmethod
    def value_of(cls, value: 'Color') -> 'Color':
        """
        Return an enum object for the entered string
        """
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class SortType(Enum):
    MODEL = 1
    MILEAGE = 2
    PRICE = 3
