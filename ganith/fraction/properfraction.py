from ganith.fraction.base import Base
import math
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ganith.fraction.improperfraction import ImproperFraction
    from ganith.fraction._types import Fraction


class ProperFraction(Base):
    def __init__(self, numerator: int, denominator: int):
        super().__init__(numerator, denominator)

    def add(self, fraction: Fraction):
        fraction = fraction.get_fraction
        lcm = math.lcm(self.denominator, fraction[1])
