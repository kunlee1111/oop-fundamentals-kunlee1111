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

if __name__ == '__main__':
  # put your code that utilizes your Fraction class here
  pass
