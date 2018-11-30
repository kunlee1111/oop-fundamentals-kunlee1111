"""
------------------------------------------------------------------------------------------------------------------------
Name: Coin.py
Purpose:
    Simulates 1000 flips of a coin, and tracks total count of heads and tails.

Author: Lee.K

Created: 2018/11/30
------------------------------------------------------------------------------------------------------------------------
"""
import random
class Coin():
    """
    Class that contains three functions: intialization method, returns the value of the face. sets the value of face.
    """
    def __init__(self):     #initialization method
        self.face = 'heads' #Heads on top initially

    def get_face(self):
        """
        returns the value of the face attribute
        :return: String (heads or tails)
        """
        return self.face

    def flip(self):
        """
        randonly sets the value of the face attributes to heads ot tails
        :return: String (heads or tails)
        """
        return str(random.choice(["heads", "tails"]))

if __name__ == '__main__': #simulates 1000 flips of a coin, keeping track of total count of heads and tails.
    a = 0               #iteration variable
    total_Heads = 0     #total numer of Heads
    total_Tails = 0     #total number of Tails
    coin = Coin()       #class coin variable
    while a <= 1000:
        coin.flip()     #for 1000 times, coin is flipped.
        a += 1          #increase in iteration
        if coin.get_face() == 'heads':  #if coin flipped is heads, total Heads increase by one
            total_Heads += 1
        else:                   #if coin flipped is tails, total tails increase by one
            total_Tails += 1
    print ("Total Heads Count is"+ total_Heads + "Total Tails Count is"+ total_Tails) #print the output