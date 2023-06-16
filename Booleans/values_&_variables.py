# the bool() function allows you to eval any value, and give you True or False in return
print(bool("Hello"))
print(bool(15), "\n")

# Almost any value is evaluated to True if it has some sort of content
# Any string is True, except empty strings
# Any number is True, except 0 
# Any list, tuple, set, and dictionary are True, except empty ones
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]), "\n")

# some values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}), "\n")

# one more value/object evaluates to False - if an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
    def __len__(self):
        return 0 
      
myobj = myclass()
print(bool(myobj))
