# to append elements from another list to the current list, use the extend() method
newlist = ["apples", "bananas", "pineapples", "zuccini", "tomatoes"]
print(newlist, "\n")
oldlist = ["cereal", "batteries", "pasta", "ketchup", "mustard"]
print(oldlist, "\n")
newlist.extend(oldlist)
print(newlist)

#** basically combines 

# my own practice - adding range
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.append(tropical[:2])
print(thislist)