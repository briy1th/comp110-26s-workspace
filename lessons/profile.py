
from __future__ import annotations
"""Define the Profile Class"""

#Write a class called Profile
class Profile:

    #It should have two attributes, username: str and private: bool
    username: str
    private: bool

    #Write a constructor that takes two paramenters: self and username_input: str

    def __init__(self, username_input: str):
        self.username = username_input
        self.private = True


#Write a magic method that converts Profile objects to a *readable* str
def __str__(self) -> str:
    info: str = ""
    if self.private:
        info = f"{self.username}: Private"
    else:
        info = f"{self.username}: Public"
    return info


# Write a method called tweet that takes as
#parameters self and msg: str
#If self.private is False, print the message
def tweet(self, msg: str) -> None:
        if self.private is False:
            print(msg)
    
    

