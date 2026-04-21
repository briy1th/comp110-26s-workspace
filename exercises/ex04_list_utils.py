"""EX04 - 'list' Utility Functions."""

__author__: str = "730926082"


def all(list_of_int_numbers: list[int], magic_num: int) -> bool:
    """Should return True if all numbers in the list match the magic number"""
    i: int = 0
    # if the list is empty return False
    if len(list_of_int_numbers) == 0:
        return False
    while len(list_of_int_numbers) > i:
        if list_of_int_numbers[i] != magic_num:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the biggest number in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = input[0]
    while (len(input) - 1) >= i:
        if input[i] >= max:
            max = input[i]
        i += 1
    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    "Checks to see if a list of integers is the same per index"
    i: int = 0
    # Check if both lists are empty and if they are return true
    if (len(list_1) == 0) and (len(list_2) == 0):
        return True
    # check if one is empty and therefore is not equal to other list
    if len(list_1) != len(list_2):
        return False
    while (len(list_1) - 1) >= i:i
        if list_1[i] > list_2[i]:
            return False
        elif list_1[i] < list_2[i]:
            return False
        i += 1
    return True


def extend(c: list[int], d: list[int]) -> None:
    """Add list 1 to another list"""
    i: int = 0
    while i < len(d):
        c.append(d[i])
        i += 1
