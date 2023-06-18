# list items are ordered, changeable, and allow duplicate values.
# list items are indexed, the first item has index [0], the second item has index [1], etc.
  # ordered means that the items have a defined order and it will not change.

# list items have an index:
thisList = ["apple", "banana", "cherry", "apple"]     # lists allow duplicates
print(thisList[2], "\n")


# new items added are placed at the end of the list.
print(thisList, "\n")
x = input("Enter a fruit to add to the list: ")
x = thisList.append(x)
print(thisList, "\n")
