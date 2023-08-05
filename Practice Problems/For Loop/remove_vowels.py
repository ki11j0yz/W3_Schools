#Remove all of the vowels in a string (use string below)
string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
result = ""
newstring = "".join([char for char in string if char not in ["a","e","i","o","u", "A", "E", "I", "O", "U"]])
print(newstring)
print("\n")


# code w/out list comprehension
#for i in range(len(string)):
#   if string[i] not in vowels:
#        result = result + string[i]

#print("\nAfter removing vowels: ", result)
#print("\n")


# different method of figuring out solution: 
result = [letter for letter in string if letter not in vowels]

result = ''.join(result)
print(result)