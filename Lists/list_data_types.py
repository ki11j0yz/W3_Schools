# items in a list can be of any data type, including "none"
# Data Types: 
    # int - integer
    # str - string
    # float - decimal
    # list
    # tuple
    # dict - dictionary
    # boolean - True/False
    # none

# the overriding type is list, but you can list the data type of any given element at its index: 

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(type(list1))
print(type(list1[0]), "\n")

print(list2)
print(type(list2))
print(type(list2[0]), "\n")

print(list3)
print(type(list3))
print(type(list3[0]), "\n")


# a list can contain different data types: 
list4 = ["abc", 34, True, 40, "male"]

print(list4)
print(type(list4[0]), type(list4[2]))