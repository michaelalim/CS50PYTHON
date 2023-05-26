# Limitation of capitalize() function is that it literally capitalize ONLY the first letter of the value, that means if I type michael jason, it will result to Michael jason, with the j being non-capitalized
# There is a better solution if you want the answer for each of its word to be capitalized when used on names.

name = input("What is your name? ").strip().title()
print(f"Hello, {name}")

# Writing "   kel alim    " in this example would result to "Kel Alim"

# ----------------------------------------------------------------------------------------------------------------------
