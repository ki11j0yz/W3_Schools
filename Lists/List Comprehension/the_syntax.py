# the syntax -> newlist = ['expression' for 'item' in 'iterable' if 'condition' == True]

# **Condition: 
  # the condition is like a filter that only accepts the items that valuate to True

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruit = [x for x in fruits if x != "apple"]
print(newfruit)

# the condition [if x != "apple"] will return True for all elements other than "apple", making the new list contain everythin accept "apple"

# the condition is optional and can be omitted:
veggies = ["carrots", "asparagus", "peppers", "onions", "peas"]
newveg = [x for x in veggies]
print(newveg)
print()


# **Iterable
# the iterable can be any iterable object, like a list, tuple, set or dictionary - or even a string
# you can use the range() to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

# with a condition
newlist = [x for x in range(10) if x < 5]
print(newlist)
print()

# **Expression
# the expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
  # set the values in teh new list to uppercase:
newupcase = [x.upper() for x in fruits]
newlowcase = [x.lower() for x in veggies]
print(newupcase)
print(newlowcase)
print()
