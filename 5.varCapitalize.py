# In addition to .strip() function on variables to remove whitespaces, .capitalize() function makes it so that returns by users will be caitalized automatically even if they have entered a non-capitalize answer

name = input("What is your name? ").capitalize()
print(f"Hello, {name}")

# If we enter a non-capitalize answer (for example: kel), it will result to Kel
# NOTE that without .strip() and if the user has answered with a whitespace before their name, it will result to the whitespace being capitalized, hence will result to the real answer not capitalized

# ----------------------------------------------------------------------------------------------------------------------

# If we try to combine the two:

bestfriend = input("What is your bestfriend's name? ").strip().title()
print(f"Hello to your friend, {bestfriend}")

# This combination of variable.strip().capitalize() should result to a well-done return of no whitespaces and cpaitalized answer
# In this example, answering "         name    " will result to "Name"

# ----------------------------------------------------------------------------------------------------------------------

# NOTE Comments are code
# We could also do:
# name = input("What is your name? ")
# name = name.strip()
# name = name.capitalize()
# print(f"Hello, {name}")
