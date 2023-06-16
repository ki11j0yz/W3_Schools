# you can return a range of characters by using the slice syntax
# the first character has index '0'
# syntax: <string name>[start : stop : step]
# step: number of characters to be skipped during slicing

b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(b))

# general slicing
print(b[2:5])

# slicing from the start
print(b[:13])
print(b[:12])
print(b[:11])
print(b[:10])

# slicing to the end
print(b[2:])

# negative indexing
print(b[-5:-2])
print(b[-8:-1])

# step slicing
print(b[2:10:2])
print(b[::1])
print(b[::-1])

# practice
txt = "Hello World!"
print(len(txt), "\n")
print(txt, "\n")
print(type(txt), "\n")
txt = txt[::-1]
print(txt, "\n")
