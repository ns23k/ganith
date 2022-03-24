from .improperfraction import ImproperFraction
from ganith.fraction.properfraction import ProperFraction


def eval_fraction(numerator, denominator):
    if numerator < denominator:
        return ImproperFraction(numerator, denominator)
    else:
        return ProperFraction(numerator, denominator)


def prettify(numerator: int, denominator: int):
    return f"""{numerator}
                """