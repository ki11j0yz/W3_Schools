# with the continue statement, you can stop the current iteration of the loop, and continue with the next: 
veggies = ["broccoli", "carrots", "asparagus", "peppers", "corn", "green beans"]
for x in veggies: 
    if x == "peppers":
        continue
    print(x)      # it skipped 'peppers' and continued on to the end of the list - you stopped the 'peppers' iteration
print("\n")


# the 'continue' and print statement are reversed in this example - see how the output changes
fruits = ["apples", "banana", "pear", "watermelon", "papaya"]
for y in fruits:
    if y == "watermelon":
        print(y)
    continue    # if the 'continue' and print statement were reversed, the output would be the same as the code above

    