# the len() function determines how many items are in a list:

thisList = ["apple", "banana", "cherry"]
print(thisList)
print(len(thisList))

# if you were to add to the list:
newListItem = input("Enter a fruit: ")
print(newListItem)                            # this will print "pear"
newListItem = thisList.append(newListItem)
print(newListItem)                            # this will print "none"
print(thisList)
print(len(thisList))
