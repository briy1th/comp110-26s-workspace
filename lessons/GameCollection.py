from __future__ import annotations
"""Class writing and instantiation."""

# Write a class called GameCollection
class GameCollection:

    #It should have three attributes: inventory, wishlist, and budget. Inventory and wishlist should be lists of strings, and budget should be a float.
    inventory: list[str]
    wishlist: list[str]
    budget: float

    #Write a constructor that takes four paremters: self, curr_inventory: list[str], wish: list[str], start_budget:float
    def __init__(self, curr_inventory: list[str], wish: list[str], start_budget:float):
        """Constructor for GameCollection."""
        self.inventory = curr_inventory
        self.wishlist = wish
        self.budget = start_budget

    # Write a method called purchase that takes as parameters self, name: str, and cost: float

    def purchase(self, name: str, cost: float) -> None:
        """Purchase a game if it is in the wishlist and there is enough budget."""
        #If cost is less than the budget attribute:
        if cost < self.budget:
            #subtract cost from the budget
            self.budget -= cost
            #add name to inventory
            self.inventory.append(name)
            #remove name from wishlist if it is in the wishlist
            idx: int = 0
            while idx < len(self.wishlist):
                curr_game: str = self.wishlist[idx]
                if curr_game == name:
                    self.wishlist.pop(idx)
                idx += 1
        #cost is greater than the budget attribute:
        else:
            print("Sorry! Not enough money!")

    #Write an __add__ magic method that takes as parameters self, new_game: str and returns a new GameCollection object with the same attribute values as self but with new_game added to the wishlist
    def __add__(self, new_game: str) -> GameCollection:
        """Add a game to the wishlist."""
        new_wishlist: list[str] = []
        #Copy over self.wishlist
        for item in self.wishlist:
            new_wishlist.append(item)
        new_collection: GameCollection = GameCollection(self.inventory, new_wishlist, self.budget)
        return new_collection

#Instantiation
my_games: GameCollection = GameCollection(["Sims"],["Witcher"], 50.75)
my_games.purchase("Witcher", 60.00)
my_games.purchase("Stardew", 40.25)
# python -m  lessons.GameCollection
ryans_games: GameCollection = my_games + "Mario"

print(ryans_games.wishlist)
print(my_games.wishlist)





