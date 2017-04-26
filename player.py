import math
import string
import random

class Player():
    """ Class for a player in the game """

    def __init__(self, position, bt=25, bats="R", era=6, power=0, speed=0, contact=0, defense=0 ):
        """ Creates a player and that players base stats """
        rng = random.Random()
        self.id = rng.getrandbits(8)
        self.bt = bt
        self.bats = bats
        self.power = power
        self.speed = speed
        self.contact = contact
        self.defense = defense
        self.position = position
        self.era = era


