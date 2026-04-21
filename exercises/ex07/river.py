"""River class and more."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730926082"


class River:
    """The river has many characteristics."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Constuctor for river class!."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """As animal's age, remove them from river."""
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for bears in self.bears:
            if bears.age <= 5:
                new_bears.append(bears)
        self.bears = new_bears

    def bears_eating(self):
        """How many fish the bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Elminate bears which starved to death."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_fish(self):
        """How many births per pair."""
        births = (len(self.fish) // 2) * 4
        for _ in range(births):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """How many birhts from bears per couple."""
        births = len(self.bears) // 2
        for _ in range(births):
            self.bears.append(Bear())

    def __str__(self) -> str:
        """View the status of your river in terms of its Fish and Bear population."""
        return (
            f"~~~ Day {self.day}: ~~~ \n"
            f"Fish Population: {len(self.fish)} \n"
            f"Bear Population: {len(self.bears)} \n"
        )

    def __add__(self, other_riv: River) -> River:
        """Add input rivers together."""
        new_river = River(
            num_fish=len(self.fish) + len(other_riv.fish),
            num_bears=len(self.bears) + len(other_riv.bears),
        )
        new_river.fish = self.fish + other_riv.fish
        new_river.bears = self.bears + other_riv.bears

        new_river.day = 0
        return new_river

    def __mul__(self, factor: int) -> River:
        """Factor by river input."""
        new_river = River(
            num_fish=len(self.fish) * factor, num_bears=len(self.bears) * factor
        )
        new_river.fish = self.fish * factor
        new_river.bears = self.bears * factor

        new_river.day = 0

        return new_river

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Call one_river_day() seven times."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Remove fish from river."""
        for _ in range(amount):
            self.fish.pop(0)
