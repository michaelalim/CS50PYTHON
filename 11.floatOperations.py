# FLOAT AND ROUND FUNCTIONS

# FLOAT

# We have to realize that int() would not support any values given by the user which has a decimal number in it
# We could make a little tweak and use float() to have it supported
# NOTE (I believe this would require a little bit more data or will slow down the process if you continuously use float, short examples are okay but big projects, we might want to carefully identify which data requires float() and which requires int())

x = float(input("What is the first number? "))
y = float(input("What is the second number? "))

print(f"The sum of the two numbers are: {x + y}")

# ----------------------------------------------------------------------------------------------------------------------

# ROUND

# We could do round off with floats and also modify with how many decimal places we would like it to have

# First example

z = round(x + y)

print(f"The rounded off sum of x and y is {z}")

# Works perfectly, if we input 1.1 and 2.6, it will answer 3.7 on line12 print, and 4 on line22 print

# ----------------------------------------------------------------------------------------------------------------------

# MODIFYING ROUND

z = (x / y)
print(f"The quotient of x and y not rounded off is: {z}")

# If 1.1 and 2.6 is used, this will result to 0.42307692...

z = round(x / y, 2)
print(f"Rounded off two places, the answer is: {z}")

# This should give the answer 0.42

# ----------------------------------------------------------------------------------------------------------------------

# Not using the round function, we could also limit the decimal places by one cryptic syntax

print(
    f"Quotient of two with two decimal places without using round function: {z:.2f}")

# The same function as round but another way of its syntax without using the function necessarily
