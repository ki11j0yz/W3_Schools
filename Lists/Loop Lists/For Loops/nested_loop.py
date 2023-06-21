# a nested loop is a loop inside of a loop - loop-ception
# the 'inner' loop will be executed one time for each iteration fo the 'outer loop'

adj =  ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# a good example of an inner/outer loop is the number pattern problem in Practice Problems\For Loop
  # C:\Users\jkpri\OneDrive\DevOp\Programming Notes\W3_Schools\Python\Practice Problems\For Loop\num_pattern.py