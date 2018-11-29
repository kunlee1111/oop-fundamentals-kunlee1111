class Fraction(object):
    def __int__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0:
            ValueError("denominator can't be zero")

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    def show(self):
        print(self.numerator,"/",self.denominator)
    def __add__(self, other_Fraction):
        new_Numerator = self.numerator*other_Fraction.denominator + self.denominator*other_Fraction.numerator
        new_Denominator = self.denominator*other_Fraction.denominator
        common = gcd(new_Denominator, new_Denominator)
        

if __name__ == '__main__':
  # put your code that utilizes your Fraction class here
  pass
