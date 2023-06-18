# Python collections (arrays)
# There are 4 collection data types:

# list = ordered, changeable, allows duplicates, uses []
mylist = ["male", 34, "ontario"]
print(mylist, "\n")

# tuple = ordered, unchangeable, allows duplicates, uses ()
mytuple = ("male", 34, "ontario")
print(mytuple, "\n")

# set =  unordered, unchangeable**, no duplicates, uses {}
  # **set items are unchangeable but you can remove/add items whenever you like
myset = {"male", 34, "ontario"}
print(myset, "\n")

# dictionary = ordered**, changeable, no duplicates, uses {} but with key:value pairs:
  # **as of PYTHON 3.7, dictionaries ARE ordered, in 3.6 and earlier, they are unordered
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
print(mydict)