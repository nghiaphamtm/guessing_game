from config import LOW, HIGH

MESSAGES = {
    "low": "Too low!",
    "high": "Too high!",
}

def ask_guess():
    return int(input(f"Guess {LOW}-{HIGH}: "))

def show(result, tries):
    if result == "win":
        print(f"Correct in {tries} tries!")
    else:
        print(MESSAGES[result])
