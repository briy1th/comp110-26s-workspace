"""The cool bear world."""


class Bear:
    """The bear class."""

    # Give the class bear the attributes age and hunger_score
    # Both are integers
    age: int
    hunger_score: int

    def __init__(self):
        """Intialises both self.age and hunger_score with the value 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increases the value of the age attribute by 1."""
        self.age += 1
        # Decrease hungerscore
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bear hunger score increase."""
        self.hunger_score += num_fish
