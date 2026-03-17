from random import randint, choices

class Die:
    """A class to create a dice game"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """A method that prints a random number"""
        roll = randint(1, self.sides)
        print(f"Dice has {roll}")

my_dice = Die()
my_dice.roll_die()

class Lottery:
    """A class that creates a lottery game"""

    def __init__(self, 
                 series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
                ):
        self.series = series

    def make_ticket(self):
        """A method to print a winning lottery ticket."""
        select = choices(self.series, k=4)
        print("Any ticket matching these 4 numbers or letters wins a prize:")
        print("Winning ticket:", select)
        return select

    def lottery_analysis(self):
        """A method to show how hard to win a lottery"""
        
        winning_ticket = self.make_ticket()

        my_ticket = choices(self.series, k=4)
        print("My ticket:", my_ticket)

        attempts = 0

        # Keep trying until you win
        while my_ticket != winning_ticket:
            my_ticket = choices(self.series, k=4)
            attempts += 1

        print(f"\nIt took {attempts} attempts to win!")
        

my_lottery = Lottery()
my_lottery.make_ticket()
my_lottery.lottery_analysis()


