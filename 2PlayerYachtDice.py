# 2 player yacht dice

# imports
import YachtDiceClasses as y

# initializing variables
p1ss = y.ScoreSheet()
p2ss = y.ScoreSheet()
gameDone = False
numberOfTurns = 1
d1 = y.Die()
d2 = y.Die()
d3 = y.Die()
d4 = y.Die()
d5 = y.Die()
diceKeptString = None
diceKeptList = []
inputAllInts = None
diceNotKept = [d1, d2, d3, d4, d5]
rollsDone = 0
buffer = None
validInput = None
scoringDecision = None
validChoice = None

# starting information
print("Welcome to 2 Yacht Dice! When asked \"What dice would you like to keep?\" enter the dice you'd like not to "
      "roll in a space-separated list.")
print("For example, if I wanted not to roll dice 2, 3, and 4, I would enter \"2 3 4\" at this stage. Have fun!")
p1ss.playerName = input("Player 1, what is your name?\n")
p2ss.playerName = input("Player 2, what is your name?\n")

# the game
while not gameDone:
    # player 1's turn
    rollsDone = 0  # reset rolls
    diceNotKept = [d1, d2, d3, d4, d5]  # reset list
    while rollsDone < 3 and len(diceNotKept) > 0:
        buffer = input(p1ss.playerName + ", press enter to roll!")
        for die in diceNotKept:
            die.roll()
        print("You rolled the following:")
        print(d1.value, d2.value, d3.value, d4.value, d5.value)
        rollsDone += 1
        if rollsDone < 3:
            diceKeptString = input("What dice would you like to keep?\n")
            diceKeptList = diceKeptString.split(" ")
            diceNotKept = [d1, d2, d3, d4, d5]  # reset list
            validInput = False  # reset variable
            while not validInput:
                inputAllInts = not diceKeptList[0] or all(y.RepresentsInt(i) for i in diceKeptList)
                if inputAllInts:
                    if diceKeptList[0]:  # case where player wants to save some dice
                        diceKeptList = list(dict.fromkeys(diceKeptList))  # removes repeating elements
                        diceKeptList = [int(i) - 1 for i in diceKeptList]  # minus one bc of the 0 index in python
                        inputAllInts = all(0 <= i <= 4 for i in diceKeptList)  # reusing this variable to see if ints
                        # are in correct range
                        if inputAllInts:
                            validInput = True
                            for i in sorted(diceKeptList, reverse=True):
                                del diceNotKept[i]
                        else:
                            diceKeptString = input(
                                "That was an invalid input. You can only input the numbers 1 through 5. Try again.\n")
                            diceKeptList = diceKeptString.split(" ")
                    else:  # player does not want to keep any dice, so the reset list is already correct
                        validInput = True
                else:
                    diceKeptString = input(
                        "That was an invalid input. You need to input your choices as a space-separated list. Try "
                        "again.\n")
                    diceKeptList = diceKeptString.split(" ")
    print("What category would you like to put this roll towards?")
    p1ss.printScoreSheet()
    scoringDecision = input()
    validChoice = p1ss.chooseOption(scoringDecision, d1, d2, d3, d4, d5)
    while not validChoice:
        scoringDecision = input(
            "That was an invalid input. Type one of the scoring options that hasn't been chosen. Try again.\n")
        validChoice = p1ss.chooseOption(scoringDecision, d1, d2, d3, d4, d5)
    p1ss.printScoreSheet()
    # player 2's turn
    rollsDone = 0  # reset rolls
    diceNotKept = [d1, d2, d3, d4, d5]  # reset list
    while rollsDone < 3 and len(diceNotKept) > 0:
        buffer = input(p2ss.playerName + ", press enter to roll!")
        for die in diceNotKept:
            die.roll()
        print("You rolled the following:")
        print(d1.value, d2.value, d3.value, d4.value, d5.value)
        rollsDone += 1
        if rollsDone < 3:
            diceKeptString = input("What dice would you like to keep?\n")
            diceKeptList = diceKeptString.split(" ")
            diceNotKept = [d1, d2, d3, d4, d5]  # reset list
            validInput = False  # reset variable
            while not validInput:
                inputAllInts = not diceKeptList[0] or all(y.RepresentsInt(i) for i in diceKeptList)
                if inputAllInts:
                    if diceKeptList[0]:  # case where player wants to save some dice
                        diceKeptList = list(dict.fromkeys(diceKeptList))  # removes repeating elements
                        diceKeptList = [int(i) - 1 for i in diceKeptList]  # minus one bc of the 0 index in python
                        inputAllInts = all(0 <= i <= 4 for i in diceKeptList)  # reusing this variable to see if ints
                        # are in correct range
                        if inputAllInts:
                            validInput = True
                            for i in sorted(diceKeptList, reverse=True):
                                del diceNotKept[i]
                        else:
                            diceKeptString = input(
                                "That was an invalid input. You can only input the numbers 1 through 5. Try again.\n")
                            diceKeptList = diceKeptString.split(" ")
                    else:  # player does not want to keep any dice, so the reset list is already correct
                        validInput = True
                else:
                    diceKeptString = input(
                        "That was an invalid input. You need to input your choices as a space-separated list. Try "
                        "again.\n")
                    diceKeptList = diceKeptString.split(" ")
    print("What category would you like to put this roll towards?")
    p2ss.printScoreSheet()
    scoringDecision = input()
    validChoice = p2ss.chooseOption(scoringDecision, d1, d2, d3, d4, d5)
    while not validChoice:
        scoringDecision = input(
            "That was an invalid input. Type one of the scoring options that hasn't been chosen. Try again.\n")
        validChoice = p2ss.chooseOption(scoringDecision, d1, d2, d3, d4, d5)
    p2ss.printScoreSheet()
    numberOfTurns += 1
    if numberOfTurns == 2:
        gameDone = not gameDone

print("The winner is:")
if p1ss.calculateScore() > p2ss.calculateScore():
    print(p1ss.playerName + "! Congratulations!")
elif p1ss.calculateScore() < p2ss.calculateScore():
    print(p2ss.playerName + "! Congratulations!")
else:
    print('Wow! It was tie!')
