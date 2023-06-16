# format() method takes in passed arguments, formats them, and places them in the string where the {} placeholders are - it can take an unlimited number of arguments.
age = 34
txt = "My name is James, and I am {}"
print(txt.format(age,), "\n")

# multiple arguments
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item #{} for ${}."
print(myorder.format(quantity, itemno, price), "\n")


# using index {0} numbers to assure arguments are placed correctly
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay ${2} for {0} pieces of item #{1}."
print(myorder.format(quantity, itemno, price))