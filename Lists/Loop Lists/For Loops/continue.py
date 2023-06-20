# with the continue statement, you can stop the current iteration of the loop, and continue with the next: 
veggies = ["broccoli", "carrots", "asparagus", "peppers", "corn", "green beans"]
for x in veggies: 
    if x == "peppers":
        continue
    print(x)