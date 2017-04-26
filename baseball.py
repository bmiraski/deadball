from player import Player
import dice

class Base():
    """ defines the state of the bases """

    def __init__(self, occupied = False):
        """ creates a base """
        self.occupied = occupied
        self.runner = 0

first = Base()
second = Base()
third = Base()

charles = Player(6, 34, "R")
parker = Player(1, 12, "L", 2)

print(charles.id)
print(charles.bt)
print(charles.power)
print(charles.position)
print(parker.era)
print(parker.position)

def pitchdie(pitcher):
    """ Returns the pitch die for a pitcher """
    era = pitcher.era
    if era < 1:
        return 20
    elif era < 2:
        return 12
    elif era < 3:
        return 8
    elif era < 4:
        return 4
    elif era < 5:
        return 8
    elif era < 6:
        return 12
    else:
        return 20

print(pitchdie(parker))

def defroll(hitroll, hit):
    """ Determines the result of a defensive roll """
    roll = dice.die_roll(6)
    if roll == 1:
        if hit == "single":
            return "single, error"
        if hit == "double":
            return "double, error"
        if hit == "triple":
            return "triple, error"
    elif roll <=4:
        return hit
    elif roll <=5:
        if hit == "single":
            return hit
        if hit == "double":
            return "single, runners +2"
        if hit == "triple":
            return "double, runners +3"
    else:
        return outtype(hitroll)

def outtype(roll):
    """ Returns the out type """
    outtype = roll % 10
    if outtype <= 2:
        return "strikeout"
    if outtype == 3:
        return "G3"
    if outtype == 4:
        return "G4"
    if outtype == 5:
        return "G5"
    if outtype == 6:
        return "G6"
    if outtype == 7:
        return "F7"
    if outtype == 8:
        return "F8"
    else:
        return "F9"

def atbat(batter, pitcher):
    """ defines an atbat between a batter and a pitcher """
    pm = 1
    if pitcher.era >= 3.5:
        pm = -1
    roll = dice.die_roll(100) + pm * dice.die_roll(pitchdie(pitcher))

    if roll <= batter.bt:
        hitroll = dice.die_roll(20)
        if hitroll <=2:
            return "single"
        if hitroll <=7:
            return defroll(roll, "single")
        if hitroll <=12:
            return "single, runners +2"
        if hitroll <=15:
            return defroll(roll, "double")
        if hitroll <=17:
            return "double, runners +3"
        if hitroll <=18:
            return defroll(roll, "triple")
        else:
            return "Home Run"
    elif roll < (batter.bt + 5):
        return "walk"
    else:
        return outtype(roll)


for x in range(20):
    print(atbat(charles,parker))



def main():
    """ Runs the baseball game """


