# creates a shorter syntax when you want to create a new list based on the values of th an exsiting list: 
# example: 

cars = ["Corvette", "Mustang", "Chevelle", "Audi", "Lexus"]
newlist = []

for x in cars: 
    if "e" in x:
        newlist.append(x)
print(newlist)


# with list comprehension: newlist = [expression for item in iterable if condition == True]
newlist = [x for x in cars if "e" in x]
print(newlist)

# **Condition: like a filter that only accpets the items that valuate to True.
#example:
newlist = [x for x in cars if x != "Mustang"]
print(newlist)