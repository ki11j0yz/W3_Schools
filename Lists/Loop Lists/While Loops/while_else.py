# the 'else' statement can run a block of code once when the condition is no longer True

i = 1
while i < 6:
    print(i)
    i += 1
else: 
    print("'i' is no longer less than 6")

# at the very end of the code sequence, 'i' becomes equal (==) to 6 and therefore 'i' is no longer < 6
