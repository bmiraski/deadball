import random

def die_roll(x):
    """ Rolls a die with x sides """
    rng = random.Random()
    roll = rng.randint(1, x)
    return roll