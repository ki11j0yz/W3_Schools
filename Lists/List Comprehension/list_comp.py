# list comprehension can offer shorter syntax when you want to create a new list based on the values of an existing list. 

# a program without list comprehensions' syntax:
#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


# with list comprehension syntax: 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]