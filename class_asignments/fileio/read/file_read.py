file = open("products.json", "r")

file_contents = file.read()

file.close()

# prints out the whole content in python string format.
print(file_contents)

# its a string
print(type(file_contents))
