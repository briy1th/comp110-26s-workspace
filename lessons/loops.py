"""Practice using while loops to iterate over a string."""

def find_small_card(cards:str) -> int:
    """Returns the card interger of the lowest value in cards"""
    lowest_card: int = int(cards[0])
    index: int = 0
    while index < len(cards):
        current_card: int = int(cards[index])
        if current_card < lowest_card:
            lowest_card = current_card
        index = index + 1
    return lowest_card
        
find_small_card(cards="8675309")
