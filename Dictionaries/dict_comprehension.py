things = {'car': 'thing', 'Grand Canyon': 'place', 'Marlon Brando': 'Person'}
things['Space'] = 'Frontier'
print(things['Space'])
print(things, "\n")

# -> This code creates a dictionary 'things' with three key-value pairs: 'car': 'thing', 'Grand Canyon': 'place', 'Marlon Brando': 'Person'
# -> Then a new key-value pair is added: {'Space': 'Frontier'}
# -> Then the value associated with 'Space' is printed as well as the whole dictionary 'things'
# -> In Python, the keys in a dictionary must be unique and immutable (e.g. strings, numbers, tuples) while the values can be any data type.


# ** dict Data types -
# -> the items in a dict can have any data type:
a = {'one': 1, 'two': 'two', 'three': 3.0, 'four': [4, 4.0]}
print(a, "\n") 

# update 'one' to 1.0:
a['one'] = 1.0
print(a, "\n")


# -> delete key-value pair 'one' from dict things: 
del a['one']
print(a, "\n")

# -> remove all key-value pairs from the dict 'things':
things.clear()
print(things)