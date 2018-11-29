
class Fraction(object):
    def __int__(self, numerator, denominator):
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
        return str(self.numerator)+"/"+str(self.denominator)

    def __reduce(self):
        gcd = lambda m, n: m if not n else gcd(n, m % n)
        gcded = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / gcded
        self.denominator = self.denominator.gcded
        return self

    def add(self, otherFraction):
        self.numerator = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
        self.denominator = self.denominator * otherFraction.denominator

    def subtract(self, otherFraction):
        self.numerator = self.numerator*otherFraction.denominator-otherFraction.numerator*self.denominator
        self.denominator = self.denominator+otherFraction.denominator

    def multiply(self, otherFraction):
        self.numerator = self.numerator*otherFraction.numerator
        self.denominator = self.denominator*otherFraction.denominator
g