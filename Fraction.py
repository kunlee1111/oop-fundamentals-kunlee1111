"""
------------------------------------------------------------------------------------------------------------------------
Name: Fraction.py
Purpose:
    Output the result of adding, subtracting, and multiplying the two fractions.

Author: Lee.K

Created: 2018/11/30
------------------------------------------------------------------------------------------------------------------------
"""
class Fraction(object):
    """
    models a fraction object
    """
    def __init__(self, numerator, denominator):
        """
        constructor method, initializes the numerator and denominator attributes based.
        :param numerator: int. The numerator of fraction
        :param denominator: int. The denominator of fraction
        """
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ValueError("denominator can't be zero")

    def get_numerator(self):
        """
        returns the value of the numerator attribute
        :return: int. numerator
        """
        return self.numerator

    def get_denominator(self):
        """
        returns the value of the denominator attribute
        :return: int. denominator
        """
        return self.denominator

    def set_numerator(self, new_numerator):
        """
        set the value of the numerator attribute to the int parameter new_numerator.
        :param new_numerator: the new-made numerator of a new fraction
        """
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):
        """
        set the value of the denominator attribute to the int parameter new_denominator
        :param new_denominator: the new-made denominator of a new fraction
        :return: int. new_denominator. Error if is 0 
        """
        self.denominator = new_denominator
        if self.denominator == 0:
            raise ValueError("denominator can't be zero")

    def __str__(self):
        """
        returns the fraction in string form
        :return: str. fraction
        """
        return "{}/{}".format(int(self.numerator), int(self.denominator))

    def __reduce(self):
        """
        Reduces the fraction to lowest terms
        :return: int. fraction simplified
        """
        gcd = lambda m, n: m if not n else gcd(n, m % n)
        gcded = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / gcded
        self.denominator = self.denominator / gcded
        return self

    def add(self, otherFraction):
        """
        adds otherFraction to the current Fraction. Reduces the lowest terms if necessary.
        :param otherFraction: int. new made fraction
        :return: int. added fraction, reduced
        """
        self.numerator = (
            self.numerator * otherFraction.denominator
            + otherFraction.numerator * self.denominator
        )
        self.denominator = self.denominator * otherFraction.denominator
        self.__reduce()
        return self

    def subtract(self, otherFraction):
        """
        substraces otherFraction to the current Fraction. Reduces the lowest terms if necessary.
        :param otherFraction: int. new made fraction
        :return: int. subtracted fraction, reduced
        """
        self.numerator = (
            (self.numerator * otherFraction.denominator)
            - (otherFraction.numerator * self.denominator)
        )
        self.denominator = self.denominator * otherFraction.denominator
        self.__reduce()
        return self

    def multiply(self, otherFraction):
        """
        multiplies otherFraction to the new current Fraction. Reduces the lowest terms if necessary.
        :param otherFraction: int. new made fraction
        :return: int. multiplied fraction, reduced
        """
        self.numerator = self.numerator * otherFraction.numerator
        self.denominator = self.denominator * otherFraction.denominator
        self.__reduce()
        return self


if __name__ == "__main__":
    print("** Fraction 1 **")   #prints to indicate the first fraction to be input.
    numerator = int(input("Enter the numerator:"))    #user interger input for numerator
    denominator = int(input("Enter the denominator:")) #user interger input for denominator
    fraction1 = Fraction(numerator, denominator)     #fraction variable using two chosen variables
    print("** Fraction 2 **")   #prints to indicate the new fraction to be input.
    numerator = int(input("Enter the numerator:"))  #user interger input for new numerator
    denominator = int(input("Enter the denominator:"))  #user interger input for new denominator
    fraction2 = Fraction(numerator, denominator)    #new fraction varuable using the new numerator and denominator
    print("{} + {} = {}".format(fraction1,fraction2,fraction1.add(fraction2))) #prints the added formula
    print("{} - {} = {}".format(fraction1,fraction2,fraction1.subtract(fraction2))) #prints the subtracted formula
    print("{} * {} = {}".format(fraction1,fraction2,fraction1.multiply(fraction2))) #prints the multiplied formula

    pass