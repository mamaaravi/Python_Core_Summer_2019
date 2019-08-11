def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

print(greet("David"))
print(greet("Johnny"))

# Output sample:

# Hello, David!
# Hello, my love!