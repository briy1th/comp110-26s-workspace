from lessons.profile import Profile



"""Instatiate the Profile Class."""

#Create a variable user1 that is reference
#To a Profile object with the username 110_rulez

user1: Profile = Profile("110_rulez")
print(user1.private)
#python -m lessons.posts_feed 

#Update user1's private attribute to False
user1.private = False
print(user1.private)

#Use the tweet method call to tweet the message OOP is cool!
#two args: user1, "OOP is cool!"
user1.tweet("OOP is cool!")


str(user1) # calls __str__ method, which is a magic method that converts the object to a readable string
print(user1) # calls __str__ mehtod and prints the result, which is a readable string representation of the object


