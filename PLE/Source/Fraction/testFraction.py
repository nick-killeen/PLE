# Fraction/testFraction.py
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for Fraction.py.

import Fraction;
import Fraction.Fraction as Fraction;

def testFraction():
    # test constructor __init__, getNumerator, and getDenominator
    fraction1 = Fraction.Fraction("chopped capsicum", "diced tomato");
    assert(fraction1.getNumerator() == "chopped capsicum");
    assert(fraction1.getDenominator() == "diced tomato");

    fraction2 = Fraction.Fraction("shredded chicken", 
        "shredded chicken");
    assert(fraction2.getNumerator() == "shredded chicken");
    assert(fraction2.getDenominator() == "shredded chicken");
