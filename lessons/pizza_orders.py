"""Practice the basic syntax of OOP in Python."""

# Define a class called Pizza

class Pizza: #Pizza does not have to be capitalized

    gluten_free: bool
    size: str
    toppings: int

    def __init__(self, gf: bool sz: str, top: int):
        self.gluten_free = gf
        self.size = sz
        self.toppings = top
        #return self

#Instantiate a class

bryanna_order: Pizza = Pizza(False, "small", 2) # <- Constructor
nules_order: Pizza = Pizza(True, "large", 5) 
#bryanna_order.gluten_free = False
#bryanna_order.size = "small"
#nules_order.size = "large"
#bryanna_order.toppings = 2
#nules_order.toppings = 5
print(bryanna_order.size)
print(nules_order.size)


def price(self) -> float:
    """Returns the price of a Pizza object."""
    total: float = 0.0
    if self.size == "small":
        total= 5.25
    else: 
        total = 7.5
    total += self.toppings * 0.25
    if self.gluten_free:
        total += 1.0   
    return total


print(nules_order.price())



# python -m lessons.pizza_orders