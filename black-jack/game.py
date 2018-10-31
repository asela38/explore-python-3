"""
 Black Jack Game
"""
class Account():
    
    def __init__(self, ammount):
        self.ammount = ammount

    def withdraw(self, ammount):
        """
            withdraw ammount
            If successful return true else return false
        """
        if self.ammount < ammount:
            print(f"Current balance {self.ammount} is not sufficent to withdraw {ammount}")
            return False

        self.ammount -= ammount
        return True

class Card():

    def __init__(self, value):
        self.value = value
    
class Hand():

    def __init__(self)
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def value(self):
        sum( 

class Person():

    def __init__(self, account):
        self.account = account

    def bet(self, ammount):
        """
            Bet ammount    
        """ 
        self.current_bet = ammount if self.account.withdraw(ammount) else 0
          
          
