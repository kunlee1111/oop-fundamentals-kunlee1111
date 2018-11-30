class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            raise ValueError("denominator can't be zero")

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, new_numerator):
        self.numerator = new_numerator

    def set_denominator(self, new_denominator):
        self.denominator = new_denominator
        if self.denominator == 0:
            raise ValueError("denominator can't be zero")

    def __str__(self):
        return "{}/{}".format(int(self.numerator), int(self.denominator))

    def __reduce(self):
        gcd = lambda m, n: m if not n else gcd(n, m % n)
        # lcm = lambda m, n: m * n / gcd(m, n)
        gcded = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / gcded
        self.denominator = self.denominator / gcded
        return self

    def add(self, otherfraction):

        self.numerator = (
            self.numerator * otherfraction.denominator
            + otherfraction.numerator * self.denominator
        )
        self.denominator = self.denominator * otherfraction.denominator
        self.__reduce()
        return self

    def subtract(self, otherfraction):

        self.numerator = (
            (self.numerator * otherfraction.denominator)
            - (otherfraction.numerator * self.denominator)
        )
        self.denominator = self.denominator * otherfraction.denominator
        self.__reduce()
        return self

    def multiply(self, otherfraction):

        self.numerator = self.numerator * otherfraction.numerator
        self.denominator = self.denominator * otherfraction.denominator
        self.__reduce()
        return self


if __name__ == "__main__":

    pass