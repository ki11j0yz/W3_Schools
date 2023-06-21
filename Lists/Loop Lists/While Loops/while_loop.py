# can execute a set of statements as long as a condition is True.
# loops through the items of a list by using a 'while' loop. 

# use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# remember to increase the index by 1 after each iteration.

mylist = ["kiwi", "pineapple", "papaya", "jackfruit", "coconut"]
i = 0
while i < len(mylist):    # the condition is either True/False - if True, then continue.
    print(mylist[i])
    i = i + 1
print()
# the while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1


# a simpler version:
i = 1
while i < 6:  # will stop printing at 5
    print(i)
    i += 1    # += is the same as i = i + 1
    