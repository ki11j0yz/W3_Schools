import time
start_time = time.time()

# This is a list that puts all of the numbers between 1 and 101 into 'newlist'

numbers = []
#for i in range(1, 101):
#    numbers.append(i)
#print(numbers)


# here it is using list comprehension - same output as code above:

numbers = [i for i in range(1, 101)]
print(numbers)



print (time.time() - start_time, 's')