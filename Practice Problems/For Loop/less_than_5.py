#                           Find all of the words in a string that are less than 5 letters

string = "Practice Problems to Drill List Comprehension in Your Head."
newstring = string.split()      # splits the words in the string into separate strings in a list   
print(newstring)                
print("\n")

# negative list comprehension
#for i in words: 
#    if len(i) <= 5:
#        words.remove(i)
#    print(words)
#print("\n")


# list comprehension
answer = [i for i in newstring if len(i) < 5]
print(answer)