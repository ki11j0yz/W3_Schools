#Find all of the numbers from 1–100 that are divisible by 8

newlist = []
#for i in range(1, 101):
#    if i % 8 == 0:
#        numbers.append(i)
#print(numbers)

# list comprehenshion: 
newlist = [i for i in range(1, 101) if i % 8 == 0]
print(newlist)