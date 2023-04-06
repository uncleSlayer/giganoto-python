file = open("products.json", "r")

# when its readline the content is string and when its readlines its a list of strings
content = file.readlines()

# content is a list of strings and when I iterate through this list i get all the strings in there
print(type(content))

file.close()