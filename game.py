import random

from config import LOW, HIGH

class Game:
    """Holds the secret number and answers guesses."""

    def __init__(self):
        self.secret = random.randint(LOW, HIGH)
        self.tries = 0

    def check(self, number):
        self.tries += 1
        if number < self.secret:
            return "low"
        if number > self.secret:
            return "high"
        return "win"
