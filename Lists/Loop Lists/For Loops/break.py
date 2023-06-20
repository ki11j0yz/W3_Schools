# the break statement can stop the loop before it has looped through all the items: 
fruits = ["apple", "banana", "cherry"]
for x in fruits: 
    print(x)
    if x == "banana":
        break
print("\n")
      
veggies = ["broccoli", "carrots", "asparagus", "peppers", "corn", "green beans"]
for x in veggies:
    print(x)
    if x == "peppers":
        break
      
      
# break comes before the print statement: here it stops and does not print out 'peppers'
veggies = ["broccoli", "carrots", "asparagus", "peppers", "corn", "green beans"]
for x in veggies:
    if x == "peppers":
        break
    print(x)      # **here you are still a part of the 'if' statement, it will run once (?)
      