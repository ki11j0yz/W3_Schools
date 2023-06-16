# built-in methods to manipulate strings: 

# Uppercase
a = "Hello, World! "
print(a.upper())

# lowercase
print(a.lower())

# Remove whitespace - the space before and/or after the actual text
print(a.strip())

# Replace string
print(a.replace("H", "J"))      # here 'H' is being replaced with 'J'

# split string - returns list where text between specified separator becomes the list items
print(a.split(","))     # returns ['Hello', 'World!']
b = "Hello World!"
print(b.split())

# list of more: https://www.w3schools.com/python/python_ref_string.asp