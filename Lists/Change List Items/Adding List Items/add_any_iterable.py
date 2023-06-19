# the extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries, etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist, "\n")


# with dictionary - since they didn't provide their own example of what it would look like: 
mylist = ["apple", "banana", "cherry"]
thisdict = {
  "fruit": "kiwi",
  "veggie": "broccoli"
}
mylist.append(thisdict)
print(mylist)
