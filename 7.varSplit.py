# We can do multiple variable assignment USING split

name = input("What is your name? ").strip().title()

# Here, we will assign the name to first name and last name
# The " " indicates that we would like to strip off from once space, we could do splits of letters by indicating "" instead of " "

firstname, lastname = name.split(" ")

print(f"Hello, {firstname}. I believe your last name is {lastname}.")
