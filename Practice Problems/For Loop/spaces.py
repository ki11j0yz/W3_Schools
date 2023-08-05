# Count the number of spaces in a string
newlist = [i for i in range(1, 101) if "6" in str(i)]
newlist = " ".join(str(i) for i in newlist)
final_list = len([i for i in newlist if i == " "])
print(final_list)

# THE WORK

#count = 0
#newlist = [i for i in range(1, 101) if "6" in str(i)]
#string = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p"
#newlist = map(str, newlist)
#newlist = list(newlist)
#newlist = " ".join(str(i) for i in newlist)
#print(newlist)

#print(len(newlist))

# attempt at converting numbers in list type to a string
#" ".join(list(newlist))
#print(list(newlist))

# driver code
#for i in range(0, len(newlist)):
#    if newlist[i] == " ": 
#        count += 1
#print(count)

# Here's the list comprehension
#final_list = len([i for i in newlist if i == " "])
#print(final_list)

#finding if spaces exist in string
#if " " in string:
#    print(True)

# prints # of characters, 1 by 1 on newline - increments. 
#for i in range(0, len(string)):
#    print(i)

