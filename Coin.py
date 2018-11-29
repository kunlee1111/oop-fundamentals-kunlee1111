import random
class Coin():
    def __init__(self):
        self.face = 'Heads'

    def get_face(self):
        return self.face

    def flip(self):
        return str(random.choice(["heads", "tails"]))

if __name__ == '__main__':
  # put your code that utilizes your Coin class here
  pass

