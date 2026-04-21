"""Making a fish class to modify the river."""


class Fish:
    """Attributes of the fish world in this fanastic river input."""

    # Give the class Fish the attribute age.

    age: int

    def __init__(self):
        """Age the fishies."""
        self.age = 0
        return None

    def one_day(self):
        """Increasing value of the age by 1."""
        self.age += 1
        return None
