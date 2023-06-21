# the else keyword in a 'for' loop specifies a block of code to be executed when the loop is finished: 
for i in range(10):
    print(i)
else:
    print("Finally finished!")
print()

# this else statement would not be executed if the loop were stopped by a 'break' statement

for x in range(6):
    if x == 3:
        break      # stops right at 3, w/out printing to stdout
    print(x)
else: 
    print("Finally finished!")
