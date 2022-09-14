"""Structured wordle."""

__author__ = 730573475

def contains_char(word: str, char: str) -> bool:
    """Checks to see if word contains specific character."""
    assert len(char) == 1
    i: int = 0
    track: int = 0 
    while len(word) > i:
        if word[track] == char:
            return True
        track += 1
        i += 1
    return False

# The emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    """To assign an emoji for each character of the guess."""
    assert len(guess) == len(secret)
    i: str = 0
    result: str = ""
    while len(secret) > i:
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result

def input_guess(length: int) -> str:
    """Makes sure user's input is valid."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program."""
    secret: str = "codes"
    turn: int = 1
    won: bool = False
    while won is False and turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True
        else:
            turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()