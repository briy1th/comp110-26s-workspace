"""Creating two use cases and one edge case for each function in dictionary.py."""


__author__: str = "730926082"


# Import the invert function from dictionary.py to test it
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Unit tests for invert
# Two use cases: General use or expected use of the function
def test_invert_use_case_1() -> None:
    """Use case: Invert a dictionary with unique values."""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}


# Same thing as one before except different values to ensure that function is working for all input 
def test_invert_use_case_2() -> None:
    """Use case: Invert a dictionary with different unique values."""
    assert invert({"yami": "20", "bryanna": "19", "bernie": "17"}) == {"20": "yami", "19": "bryanna", "17": "bernie"}


# Edge case: Case that is unexpected (not typical), but still valid input for the function
def test_invert_empty_dict() -> None:
    """Edge case: Invert an empty dictionary should return an empty dictionary."""
    assert invert({}) == {}


# Import the favorite_color function from dictionary.py to test it


# Unit tests for favorite_color
# Two use cases
def test_favorite_color_use_case_1() -> None:
    """Use case: Find the most popular color in the dictionary."""
    assert favorite_color({"Bryanna": "green", "Aubreuy": "brown", "Scarleth": "green"}) == "green"


def test_favorite_color_use_case_2() -> None:
    """Use case: Find the most popular color when there is a tie."""
    # In this case, the function should return the color that appears first in the dictionary, which is "blue"
    assert favorite_color({"Yamilet": "blue", "Bryan": "red", "Rubi": "yellow", "Michel": "purple", "Adalberta": "purple", "Bernie": "blue"}) == "blue"


# Edge case
def test_favorite_color_edge_case() -> None:
    """Edge case: Empty dictionary should return an empty string "" ."""
    assert favorite_color({}) == ""


# Import the count function from dictionary.py to test it


# Unit tests for count
# Two use cases
def test_count_use_case_1() -> None:
    """Use case: Count the frequency of values in a list."""
    assert count(["nule", "loves", "nule", "banana", "loves", "nule"]) == {"nule": 3, "loves": 2, "banana": 1}


def test_count_use_case_2() -> None:
    """Use case: Count the frequency of values in a list with unique items."""
    assert count(["yami", "hates", "me"]) == {"yami": 1, "hates": 1, "me": 1}


# Edge case
def test_count_edge_case() -> None:
    """Edge case: Count the frequency of values in an empty list should return an empty dictionary."""
    assert count([]) == {}

# Import the alphabetizer function from dictionary.py to test it


# Unit tests for alphabetizer
# Two use cases
def test_alphabetizer_use_case_1() -> None:
    """Use case: Alphabetize a list of words."""
    assert alphabetizer(["yami", "bryanna", "bryan", "bernie", "aubreuy"]) == {"y": ["yami"], "b": ["bryanna", "bryan", "bernie"], "a": ["aubreuy"]}


def test_alphabetizer_use_case_2() -> None:
    """Use case: Alphabetize a list of words with upper and lowercase to account for the case sensitivity."""
    assert alphabetizer(["Nule", "Tiffany", "Rubi", "scarleth", "valentin"]) == {"n": ["Nule"], "t": ["Tiffany"], "r": ["Rubi"], "s": ["scarleth"], "v": ["valentin"]}


# Edge case
def test_alphabetizer_edge_case() -> None:
    """Edge case: Alphabetize a list of words with non-alphabetic characters should ignore them."""
    assert alphabetizer(["123", "aubreuy", "!@#", "banana"]) == {"a": ["aubreuy"], "b": ["banana"]}


# Import the update_attendance function from dictionary.py to test it


# Unit tests for update_attendance
# Two use cases
def test_update_attendance_use_case_1() -> None:
    """Use case: Update attendance for a student on a specific day."""
    attendance = {"Monday": ["Aubreuy", "Bryanna"], "Tuesday": ["Bernie"]}
    update_attendance(attendance, "Monday", "Yamilet")

    # Yamilet is being added

    assert attendance == {"Monday": ["Aubreuy", "Bryanna", "Yamilet"], "Tuesday": ["Bernie"]}


def test_update_attendance_use_case_2() -> None:
    """Use case: Update attendance for a student on a new day."""
    attendance = {"Monday": ["Rubi", "Scarleth"], "Tuesday": ["Valentin"]}
    update_attendance(attendance, "Wednesday", "Bryanna")
    assert attendance == {"Monday": ["Rubi", "Scarleth"], "Tuesday": ["Valentin"], "Wednesday": ["Bryanna"]}

    
# Edge case
def test_update_attendance_edge_case() -> None:
    """Edge case: Update attendance with an empty attendance dictionary should add the new day and student."""
    attendance = {}
    update_attendance(attendance, "Monday", "Nule")
    assert attendance == {"Monday": ["Nule"]}