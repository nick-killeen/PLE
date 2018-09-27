# Fraction/Fraction.py
# Nicholas Killeen,
# 19th June 2016.
# Container class to store fractions involving Relations.

# Stores a numerator and a denominator.
class Fraction:
    def __init__(this, numerator, denominator):
        this.numerator = numerator;
        this.denominator = denominator;

    def getDenominator(this):
        return this.denominator;

    def getNumerator(this):
        return this.numerator;
