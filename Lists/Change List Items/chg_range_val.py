#if you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
mylist = ["apple", "banana", "cherry", "pear", "cactus"]
mylist[1:2] = ["orange", "kiwi"]
print(mylist, "\n")

# the length of the list will change when the # of items inserted does not match the # of items replaced
mylist[1:3] = ["watermelon"]
print(mylist)