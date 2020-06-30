# classes to play Yacht Dice
import random


class Die:

    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)


def sortDiceValues(a, b, c, d, e):
    listOfDiceValues = [a.value, b.value, c.value, d.value, e.value]
    listOfDiceValues.sort()
    return listOfDiceValues


class ScoreSheet:

    def __init__(self):
        self.playerName = None
        self.aces = [0, False]
        self.deuces = [0, False]
        self.threes = [0, False]
        self.fours = [0, False]
        self.fives = [0, False]
        self.sixes = [0, False]
        self.bonus = [0, False]
        self.choice = [0, False]
        self.fourOfKind = [0, False]
        self.fullHouse = [0, False]
        self.smallStraight = [0, False]
        self.largeStraight = [0, False]
        self.yacht = [0, False]

    def Aces(self, a, b, c, d, e):
        if not self.aces[1]:
            if a.value == 1:
                self.aces[0] += 1
            if b.value == 1:
                self.aces[0] += 1
            if c.value == 1:
                self.aces[0] += 1
            if d.value == 1:
                self.aces[0] += 1
            if e.value == 1:
                self.aces[0] += 1
            self.Bonus()
            self.aces[1] = True
            return True
        else:
            return False

    def Deuces(self, a, b, c, d, e):
        if not self.deuces[1]:
            if a.value == 2:
                self.deuces[0] += 2
            if b.value == 2:
                self.deuces[0] += 2
            if c.value == 2:
                self.deuces[0] += 2
            if d.value == 2:
                self.deuces[0] += 2
            if e.value == 2:
                self.deuces[0] += 2
            self.Bonus()
            self.deuces[1] = True
            return True
        else:
            return False

    def Threes(self, a, b, c, d, e):
        if not self.threes[1]:
            if a.value == 3:
                self.threes[0] += 3
            if b.value == 3:
                self.threes[0] += 3
            if c.value == 3:
                self.threes[0] += 3
            if d.value == 3:
                self.threes[0] += 3
            if e.value == 3:
                self.threes[0] += 3
            self.Bonus()
            self.threes[1] = True
            return True
        else:
            return False

    def Fours(self, a, b, c, d, e):
        if not self.fours[1]:
            if a.value == 4:
                self.fours[0] += 4
            if b.value == 4:
                self.fours[0] += 4
            if c.value == 4:
                self.fours[0] += 4
            if d.value == 4:
                self.fours[0] += 4
            if e.value == 4:
                self.fours[0] += 4
            self.Bonus()
            self.fours[1] = True
            return True
        else:
            return False

    def Fives(self, a, b, c, d, e):
        if not self.fives[1]:
            if a.value == 5:
                self.fives[0] += 5
            if b.value == 5:
                self.fives[0] += 5
            if c.value == 5:
                self.fives[0] += 5
            if d.value == 5:
                self.fives[0] += 5
            if e.value == 5:
                self.fives[0] += 5
            self.Bonus()
            self.fives[1] = True
            return True
        else:
            return False

    def Sixes(self, a, b, c, d, e):
        if not self.sixes[1]:
            if a.value == 6:
                self.sixes[0] += 6
            if b.value == 6:
                self.sixes[0] += 6
            if c.value == 6:
                self.sixes[0] += 6
            if d.value == 6:
                self.sixes[0] += 6
            if e.value == 6:
                self.sixes[0] += 6
            self.Bonus()
            self.sixes[1] = True
            return True
        else:
            return False

    def Bonus(self):
        if self.aces[0] + self.deuces[0] + self.threes[0] + self.fours[0] + self.fives[0] + self.sixes[0] >= 63:
            self.bonus = [35, True]

    def Choice(self, a, b, c, d, e):
        if not self.choice[1]:
            self.choice[0] = a.value + b.value + c.value + d.value + e.value
            self.choice[1] = True
            return True
        else:
            return False

    def FourOfKind(self, a, b, c, d, e):
        if not self.fourOfKind[1]:
            sortedDiceValues = sortDiceValues(a, b, c, d, e)
            if sortedDiceValues[1] == sortedDiceValues[2] == sortedDiceValues[3] and (
                    sortedDiceValues[0] == sortedDiceValues[2] or sortedDiceValues[4] == sortedDiceValues[2]):
                self.fourOfKind[0] = sortedDiceValues[2] * 4
            self.fourOfKind[1] = True
            return True
        else:
            return False

    def FullHouse(self, a, b, c, d, e):
        if not self.fullHouse[1]:
            sortedDiceValues = sortDiceValues(a, b, c, d, e)
            if sortedDiceValues[0] == sortedDiceValues[1] and sortedDiceValues[3] == sortedDiceValues[4] and (
                    sortedDiceValues[2] == sortedDiceValues[3] or sortedDiceValues[2] == sortedDiceValues[1]):
                self.fullHouse[0] = a.value + b.value + c.value + d.value + e.value
            self.fullHouse[1] = True
            return True
        else:
            return False

    def SmallStraight(self, a, b, c, d, e):
        if not self.smallStraight[1]:
            sortedDiceValues = sortDiceValues(a, b, c, d, e)
            sortedDiceValues = list(dict.fromkeys(sortedDiceValues))  # removes repeating elements
            if len(sortedDiceValues) == 4 and sortedDiceValues[0] == sortedDiceValues[1] - 1 == sortedDiceValues[
                2] - 2 == sortedDiceValues[3] - 3:
                self.smallStraight[0] = 15
            elif len(sortedDiceValues) == 5:
                if sortedDiceValues[0] == sortedDiceValues[1] - 1 == sortedDiceValues[2] - 2 == sortedDiceValues[3] - 3:
                    self.smallStraight[0] = 15
                elif sortedDiceValues[1] == sortedDiceValues[2] - 1 == sortedDiceValues[3] - 2 == sortedDiceValues[
                    4] - 3:
                    self.smallStraight[0] = 15
            self.smallStraight[1] = True
            return True
        else:
            return False

    def LargeStraight(self, a, b, c, d, e):
        if not self.largeStraight[1]:
            sortedDiceValues = sortDiceValues(a, b, c, d, e)
            if sortedDiceValues[0] == sortedDiceValues[1] - 1 == sortedDiceValues[2] - 2 == sortedDiceValues[3] - 3 == \
                    sortedDiceValues[4] - 4:
                self.largeStraight[0] = 30
            self.largeStraight[1] = True
            return True
        else:
            return False

    def Yacht(self, a, b, c, d, e):
        if not self.yacht[1]:
            if a.value == b.value == c.value == d.value == e.value:
                self.yacht[0] = 50
            self.yacht[1] = True
            return True
        else:
            return False

    # dictionary placed outside chooseOption function so the dictionary doesnt have to made every time the function
    # is called
    options = {
        "aces": Aces,
        "deuces": Deuces,
        "threes": Threes,
        "fours": Fours,
        "fives": Fives,
        "sixes": Sixes,
        "choice": Choice,
        "four of a kind": FourOfKind,
        "full house": FullHouse,
        "small straight": SmallStraight,
        "large straight": LargeStraight,
        "yacht": Yacht
    }

    def chooseOption(self, option, a, b, c, d, e):
        if option in self.options:
            notYetChosen = self.options[option](self, a, b, c, d, e)
            if notYetChosen:
                return True
            else:
                return False
        else:
            return False

    def printScoreSheet(self):
        print("\n" + self.playerName + "'s Scoresheet")
        if self.aces[1]:
            print("Aces:", self.aces[0])
        else:
            print("Aces: available")
        if self.deuces[1]:
            print("Deuces:", self.deuces[0])
        else:
            print("Deuces: available")
        if self.threes[1]:
            print("Threes:", self.threes[0])
        else:
            print("Threes: available")
        if self.fours[1]:
            print("Fours:", self.fours[0])
        else:
            print("Fours: available")
        if self.fives[1]:
            print("Fives:", self.fives[0])
        else:
            print("Fives: available")
        if self.sixes[1]:
            print("Sixes:", self.sixes[0])
        else:
            print("Sixes: available")
        if self.bonus[1]:
            print("Bonus:", self.bonus[0])
        else:
            print("Bonus: 0 \nGet a total of 63 in above categories to get a 35 point bonus! Total progress: " + str(
                self.aces[0] + self.deuces[0] + self.threes[0] + self.fours[0] + self.fives[0] + self.sixes[0]))
        if self.choice[1]:
            print("Choice:", self.choice[0])
        else:
            print("Choice: available")
        if self.fourOfKind[1]:
            print("Four of a kind:", self.fourOfKind[0])
        else:
            print("Four of a Kind: available")
        if self.fullHouse[1]:
            print("Full House:", self.fullHouse[0])
        else:
            print("Full House: available")
        if self.smallStraight[1]:
            print("Small Straight:", self.smallStraight[0])
        else:
            print("Small Straight: available")
        if self.largeStraight[1]:
            print("Large Straight:", self.largeStraight[0])
        else:
            print("Large Straight: available")
        if self.yacht[1]:
            print("Yacht:", self.yacht[0])
        else:
            print("Yacht: available")
        print("Current total score:", self.calculateScore())
        print()

    def calculateScore(self):
        totalScore = self.aces[0] + self.deuces[0] + self.threes[0] + self.fours[0] + self.fives[0] + self.sixes[0] + \
                     self.bonus[0] + self.choice[0] + self.fourOfKind[0] + self.fullHouse[0] + self.smallStraight[0] + \
                     self.largeStraight[0] + self.yacht[0]
        return totalScore


# need to use this to see if inputs are ints
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# test code
'''
a = Die()
b = Die()
c = Die()
d = Die()
e = Die()

a.roll()
b.roll()
c.roll()
d.roll()
e.roll()

a.value = 1
b.value = 3
c.value = 2
d.value = 6
e.value = 5

print(a.value, b.value, c.value, d.value, e.value)

ss = ScoreSheet("Test Player")
#ss.chooseOption("aces", a, b, c, d, e)
#ss.chooseOption("Deuces", a, b, c, d, e)
#ss.chooseOption("Threes", a, b, c, d, e)
#ss.chooseOption("FoUrs", a, b, c, d, e)
#ss.chooseOption("Fives", a, b, c, d, e)
#ss.chooseOption("Sixes", a, b, c, d, e)
#ss.chooseOption("Choice", a, b, c, d, e)
#ss.chooseOption("Four of a kind", a, b, c, d, e)
#ss.chooseOption("Full House", a, b, c, d, e)
#ss.chooseOption("Small Straight", a, b, c, d, e)
#ss.chooseOption("Large Straight", a, b, c, d, e)
#ss.chooseOption("Yacht", a, b, c, d, e)
ss.printScoreSheet()
'''
