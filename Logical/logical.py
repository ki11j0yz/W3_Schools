# used to combine conditional statements

print("\n")
obj1 = """and   -> Returns True if both statements are true
      -> x < 5 and x < 10"""
x = 4
print(obj1)
print("x =", x)
print(x < 5 and x < 10, "\n")

      
obj2 = """or    -> Returns True if one of the statements is true
      -> y < 5 or y < 10"""
y = 4  
print(obj2)
print("y =", y)
print(y < 5 or y < 10, "\n")
      
      
obj3 = """not   -> Reverse the result, returns False if the result is true
      -> not(z < 5 and z < 10)"""
z = 20
print(obj3)
print("z =", z)
print(not(z < 5 and x < 10), "\n")
    