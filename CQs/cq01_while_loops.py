"""While loops challenge question!"""

__author__ = "730926082"


def num_instances(phrase: str, search_char: str) -> int:
    """num_instances should return the count of occurrences of search_char in phrase"""
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index += 1
    return count


def get_evens(numbers: str) -> str:
    """Should return a new string containing only the even numbers in numbers"""
    evens: str = ""
    index: int = 0
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens = evens + str(numbers[index])
        index += 1
    return evens
