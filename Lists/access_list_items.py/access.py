# lists are used to store multiple items in a single variable and are created using '[]'
# lists are one of 4 data types in python, the other three are: 
  # Tuple, Set, and Dictionary

obj = ["apple", "banana", "cherry"]
print(obj, "\n")

# list items are indexed, and you can refer to them by citing the index number:
mylist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(mylist[1], "\n")


# my own practice - adding input to a list
obj1 = input("Name a vegetable: ")
obj2 = []
if obj1 != obj1.isnumeric():
    obj2.append(obj1)
    
print(obj2, "\n")