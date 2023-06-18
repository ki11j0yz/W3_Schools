# range of indexes - you can specify a range of indexes by a start and stop position:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])   # the search will start at index 2 (included), and end at 5 (not included)

print(thislist[:])  # leaving out start/end values will print whole list
print(thislist[:6]) # leaving out the start value prints from the start of the list to the end value specified
print(thislist[0:]) # leaving out the end value prints to the end of the list