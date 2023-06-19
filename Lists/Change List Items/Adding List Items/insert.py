# to insert a new list item, w/out replacing any of the existing values, we can use the insert() method which inserts a new item at the index specified: 
mylist = ["apple", "banana", "cherry", "kiwi"]
mylist.insert(2, "watermelon")
print(mylist, "\n")

# my own practice
grocery_list = ["apples", "asparagus", "lettuce", "rotini", "tomato sauce"]
print(grocery_list, "\n")
addItem = input("Would you like to add anything? \n")
if addItem == "Yes":
    newListItem = input("What would you like to add? \n")
    grocery_list.insert(5, newListItem)
    print(grocery_list)
    
    
# ** using the insert() method allows you to place whatever you're adding wherever you want - the append method just adds it to the end of the list