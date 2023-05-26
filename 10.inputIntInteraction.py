# Here, we will try the interaction between input() and integers

x = input("What is the first number? ")
y = input("What is the second number? ")

print(f"The sum of x and y is (string not converted): {x + y}")

# This will give answer of combining two strings, like 1 + 2 = 12
# Basically, input() always returns strings

# ----------------------------------------------------------------------------------------------------------------------

# TO FIX IT
# We have to convert strings to int by using int() function

print(
    f"The sum of x and y which we converted from string to int is: {int(x) + int(y)}")

# This now results to 1 + 2 = 3

# ----------------------------------------------------------------------------------------------------------------------

# NOTE that we could also do:
# x = int(input("What is the first number? "))
