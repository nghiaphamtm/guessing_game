from game import Game
from ui import ask_guess, show

def main():
    game = Game()
    print("I'm thinking of a number.")

    while True:
        result = game.check(ask_guess())
        show(result, game.tries)
        if result == "win":
            break

if __name__ == "__&#8203;main__":
    main()
