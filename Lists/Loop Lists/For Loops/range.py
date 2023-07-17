# the range() function allows looping through code a specified number of times
# returns a sequence of numbers, starting from 0 by default, and increments 1 (by default), and ends at a specified number

for a in range(10):
    print(a)
print()

# note that range(10), the sequence stops at 9, not 10 - if you were to change to range(11) - you would print out 10.
# range(0) defaults to 0 as a starting value, however you can specify the starting value by adding a paramter: range(2, 6) which means values from 2 to 6 (excluding 6)

for b in range(2, 10):
    print(b)
print()

# range() defaults to step 1, however you can specify a step parameter as such: 

for c in range(2, 10, 3):
    print(c)
print()


# Practice
for d in range(0, 50):
    print(d)
print()

for e in range(0, 10, 2):
    print(e)
print()

for f in range(1300, 700, -100):
    print(f)
print()