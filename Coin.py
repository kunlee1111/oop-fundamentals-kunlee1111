from random import randint
class Coin():
    def __init__(self):
        self.face = 'Heads'

    def get_face(self):
        return self.face

    def flip(self):
        temporary_Variable = randint(0,1)
        if temporary_Variable == 1:
            self.face = "Heads"
        else:
            self.face = "Tails"

if __name__ == '__main__':
  # put your code that utilizes your Coin class here
  pass

