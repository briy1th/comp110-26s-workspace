"""Practice with List syntax"""
my_numbers: list[float] = [] #<- literal 
#Also okay:
# my_numbers: list[float] = list() #<- constructor 

print(my_numbers)

#add item to list
my_numbers.append(1.5)       #Method syntax, the dot is used to call a method on the list

game_points: list[int] = [102, 86, 94]
#print out 94
print(game_points[2])

#change 86 to 72
game_points[1]  = 72
print(game_points)

#not possible to change strs in list
grocery_list: list[str] = ["milk", "eggs", "bread"]
grocery_list[1] = "butter"
print(grocery_list)

len(game_points)

#remove item from list
game_points.pop(2) #<- removes the item at index 2


#lists are placed in the heap, so they are mutable and can be changed after they are created.
