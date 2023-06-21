# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# write a program to print the following number pattern using for/while loops, range(), len(): 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("Number Pattern")

# decide the row count > the above pattern contains 5 rows, obviously
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop - 5 times
for i in range(1, row+1, 1):
    # run inner loop i+1 times
    for j in range(1, i+1):
        print(j, end=' ')
    # empty line after each row
    print("")