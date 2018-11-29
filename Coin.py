import random
class Coin():
    def __init__(self):
        self.face = 'heads'

    def get_face(self):
        return self.face

    def flip(self):
        return str(random.choice(["heads", "tails"]))

if __name__ == '__main__':
    a = 0
    total_Heads = 0
    total_Tails = 0
    coin = Coin()
    while a <= 1000:
        coin.flip()
        a += 1
        if coin.get_face() == 'heads':
            total_Heads += 1
        else:
            total_Tails += 1
    print ("Total Heads Count is"+ total_Heads + "Total Tails Count is"+ total_Tails)