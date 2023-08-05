#Find all of the numbers from 1–1000 that have a 6 in them

newlist = [i for i in range(1, 101) if "6" in str(i)]
print(newlist)