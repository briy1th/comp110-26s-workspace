""" "EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730926082"


def main() -> None:  # Based on ex01 main should be on top
    contains_char(
        input_word(), input_letter()
    )  # word= not needed due to positional agruments


def input_word() -> str:
    """Prompt the user for a 5-character word."""
    word: str = input("Enter a 5-character word: ")  # declared a variable
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # makes program not continue to run if criteria not met
    return word


def input_letter() -> str:
    """Prompt user to enter a single character"""
    letter: str = input("Enter a single character:")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(
    word: str, letter: str
) -> None:  # Remember if return type is none then there should be no return
    """Matching the character to word"""
    print(
        "searching for", letter, "in", word
    )  # I like using commas but I am unsure if it causes problems
    instances = 0  # This line is used to start the counting!
    if letter == word[0]:
        print(letter, "found at index 0")
        instances = (
            instances + 1
        )  # Learned in CLO5. The same variable can change to a different variable.
    if letter == word[1]:
        print(letter, "found at index 1")
        instances = instances + 1
    if letter == word[2]:
        print(letter, "found at index 2")
        instances = instances + 1
    if letter == word[3]:
        print(letter, "found at index 3")
        instances = instances + 1
    if (
        letter == word[4]
    ):  # I was copy-pasting these lines to make it easier but forgot to change index
        print(letter, "found at index 4")
        instances = instances + 1
    if instances == 0:
        print(
            "No instances of", letter, "found in", word
        )  # Lines before show if there are 1-5 instances. Need to do same for 0.
    elif instances == 1:
        print(
            "1 instance of", letter, "found in", word
        )  # Why can the program not be 0 and everything else instead of 0,1,2+?

    else:
        print(instances, "instances of", letter, "found in", word)


if __name__ == "__main__":
    main()
