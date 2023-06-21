# list comprehension offers the shortest syntax for looping through lists:
mylist = ["apple", "banana", "cherry"]
[print(x) for x in mylist]
print()

# the above code is the same as writing:
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

# say you had a list of fruits, and you wanted to add all of the elements with the letter 'a' of that list into a new list: if you wrote a 'for loop'
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)
print()

# but with list comprehension, you only need one line
newlist = [x for x in fruits if "a" in x]
print(newlist)
