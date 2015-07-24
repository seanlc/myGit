import random
import time
class Die(object):
    """ single six sided die that randomly generates a value when rolled"""
    dieNumber = 1
    def __init__(self):
        self.name = "Die Number " + str(self.dieNumber)
        self.value = 0
        Die.dieNumber += 1
    def __str__(self):
        return self.name + " rolled a " + str(self.value)
    def __lt__(self, other):
        return self.value < other.value
    def rollDie(self):
        self.value = random.choice([1,2,3,4,5,6])
        print self
    def getValue(self):
        return self.value
class Player(object):
    """  class which holds relevant information for players in game """
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.bank = 500
    def __str__(self):
        return self.name
    def __lt__(self, other):
        return self.score < other.score
    def setScore(self, s):
        self.score = s
    def getScore(self):
        return self.score
    def getName(self):
        return self.name
    def getBank(self):
        return self.bank
    def setBank(self, s):
        self.bank = s
class ceeLoGame(object):
    """ class which contains all necessary attributes and methods to play CeeLo, including the scoring rules """
    def __init__(self, players):
        self.die1 = Die()
        self.die2 = Die()
        self.die3 = Die()
        self.dice = [self.die1, self.die2, self.die3]
        self.players = players
        self.pot = 0
        self.repeat = False
    def roll(self):
        for roller in self.players:
            print roller.getName() + " is rolling"
            time.sleep(1)
            print ""
            validScore = False
            while not validScore:
                for die in self.dice:
                    die.rollDie()
                print ""
                if self.die1.getValue() == self.die2.getValue() and self.die2.getValue() == self.die3.getValue():
                    if self.die1.getValue() == 1:
                        roller.setScore(-1)
                        print roller.getName() + " rolled triple 1. Loser!"
                        validScore = True
                    elif self.die1.getValue() == 6:
                        roller.setScore(777)
                        print roller.getName() + " rolled triple 6. Winner!"
                        validScore = True
                    else:
                        roller.setScore(self.die1.getValue() * 100)
                        print roller.getName() + " rolled triple " + str(self.die1.getValue())
                        validScore = True
                elif self.die1.getValue() == self.die2.getValue():
                    roller.setScore(self.die3.getValue())
                    print roller.getName() + " rolled a point of " + str(self.die3.getValue())
                    validScore = True
                elif self.die1.getValue() == self.die3.getValue():
                    roller.setScore(self.die2.getValue())
                    print roller.getName() + " rolled a point of " + str(self.die2.getValue())
                    validScore = True
                elif self.die2.getValue() == self.die3.getValue():
                    roller.setScore(self.die1.getValue())
                    print roller.getName() + " rolled a point of " + str(self.die1.getValue())
                    validScore = True
                time.sleep(2)
    def getWinner(self):
        time.sleep(1)
        players.sort()
        winner = self.players[len(players) - 1]
        winner.setBank(winner.getBank() + self.pot)
        self.pot = 0
        print winner.getName() + " wins!"
    def betting(self):
        for roller in self.players:
            validBet = False
            while not validBet:
                bet = int(raw_input("How much is " + str(roller.getName()) + " betting? "))
                if roller.getBank() >= bet:
                    roller.setBank(roller.getBank() - bet)
                    self.pot += bet
                    validBet = True
                else:
                    print roller.getName() + " doesn't have that much money"
    def displayBanks(self):
        for roller in self.players:
            print roller.getName() + " -------- Bank: " + str(roller.getBank())
    def play(self):
        if not self.repeat:
            self.displayBanks()
        self.betting()
        self.roll()
        self.getWinner()
        self.displayBanks()
        answer = raw_input("Enter'p' to play again: ")
        if answer.lower() == 'p':
            self.repeat = True
            self.play()
Tony = Player("tony")
Mitch = Player("mitch")
players = [Tony, Mitch]
myGame = ceeLoGame(players)
myGame.play()