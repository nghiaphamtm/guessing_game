# Guess the Number

A tiny command-line number guessing game written in plain Python — no dependencies, no install step.

The computer picks a random number between `LOW` and `HIGH`, and you keep guessing until you hit it. After each guess it tells you whether you were too low or too high.

## Requirements

Python 3.8 or newer. Nothing else.

## Run it

cd guess_game
python main.py

Example session:

    I'm thinking of a number.
    Guess 1-100: 50
    Too high!
    Guess 1-100: 25
    Too low!
    Guess 1-100: 37
    Correct in 3 tries!

## Files

| File | Lines | What it does |
| main.py | 18 | Entry point — runs the game loop |
| game.py | 20 | The `Game` class: picks the secret number, checks guesses |
| ui.py | 18 | All input and printing |
| config.py | 2 | Tunable constants: `LOW`, `HIGH` |

## Customize

Open `config.py` and change the range:

    LOW = 1
    HIGH = 1000

That's the only file you need to touch to change the difficulty.

## Notes

- The three modules import each other by plain name (`from game import Game`), so run the game from inside the `guess_game/` folder — not from the parent directory.
- Bad input (letters, empty lines) will raise a `ValueError`. Wrapping `ask_guess()` in a `try/except` is a good first exercise if you want to harden it.
