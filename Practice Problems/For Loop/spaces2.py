# Same idea as spaces, but with user input (and not converting a type list of integers to a large string):

newlist = input("Type anything: ")
final_list = len([i for i in newlist if i == " "])
print(final_list)


# the code w/out list comprehension
#count = 0
#newlist = input("Type anything: ")
#for i in range(0, len(newlist)):
#   if newlist[i] == " ": 
#        count += 1
#print(count)