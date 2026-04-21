
from __future__ import annotations
class ShoppingGuide:

    groceries: list[str]
    budget: float
    store: str
    #Write a constructor that takes four parameters: self, groceries_input: list[str], budget_input: float, store_input: str
    def __init__(self, groceries: list[str], budget: float, store: str):
        self.groceries = groceries
        self.budget = budget
        self.store = store

    # Write a __str__ magic method that gives me all the information of a Shopping Guide Object
    def __str__(self) -> str:
        return f"Groceries: {self.groceries}, Budget: {self.budget}, Store: {self.store}"
    
    #WRITE A MAGIC METHOD __add__ that takes as parameters self, moreZ_moeny: float
    def __add__(self, more_money: float) -> ShoppingGuide:
        other_guide: ShoppingGuide = ShoppingGuide(self.groceries, self.budget + more_money, self.store)
        return other_guide
    
my_plan: ShoppingGuide = ShoppingGuide(["apples", "kiwi"], 5.55, "Food Lion")
AJs_plan: ShoppingGuide = my_plan + 2.12
    