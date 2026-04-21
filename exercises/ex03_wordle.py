"""Wordle Exercise"""

__author__ = "730926082"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False  # Winning starts false since no turns have been done
    while turn <= 6 and not won:  # not won here is more convienient than won==False
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn += 1
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # placing turn instead of X as a f string


def input_guess(secret_word_len: int) -> str:
    guess: str = input(f"Enter a {secret_word_len} character word:")
    while secret_word_len != len(guess):
        guess = input(f"That wasn't {secret_word_len} chars! Try again: {guess}")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Testing the first paramenter string to see if it matches the second parameter"""
    assert len(char_guess) == 1
    i: int = 0
    while len(secret_word) > i:
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Lists if the character is somewhere in the guess"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    answer: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            answer += (
                GREEN_BOX  # Since the string is empty this automatically adds to answer
            )
        elif contains_char(secret, guess[i]):  # This is a loop through each character!
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
        i += 1
    return answer


if __name__ == "__main__":
    main(secret="codes")
