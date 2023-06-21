# as in the 'for' loop, the break statement can stop the loop even if hte while condition is true: 

i = 1
while i < 6: 
    print(i)
    if i == 4: 
        break
    i += 1
# in the code above, you are establishing that our variable 'i' holds the value of 1 and that while it is less than 6, we want to print it but if/when i ever becomes equal to 4 we want to stop the loop all the while incrementing i by 1