from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List


class Base(object):
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return self._prettify()

    def _prettify(self):
        pass

    @property
    def get_fraction(self) -> List[int, int]:
        return [self.numerator, self.denominator]
