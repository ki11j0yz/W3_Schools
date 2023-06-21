# loop through list items  by referring to their index number - use the range() and len() functions to create a suitable iterable
mylist = ["papaya", "kiwi", "pineapple", "jackfruit"]

enumlist = enumerate(mylist)
print(list(enumlist))
print("\n")

for i in range(len(mylist)):
    print(mylist[i])
# the iterable above prints out [0, 1, 2]