# STRIP FUNCTION
# Stripping is removing whitespace on the argument
# This is a continuation of Hello, name lesson
 
# ----------------------------------------------------------------------------------------------------------------------

name = input("What is your name? ")
name = name.strip()

print(f"Hello, {name}")

# In default, if the user answers for example "   kel ", python will print "Hello,      kel  ", strip() will remove the whitespaces on the return

# ----------------------------------------------------------------------------------------------------------------------

# another way of coding it

age = input("How old are you? ").strip()

print(f"You are {age} years old")

# In this other example, we directly strip the return value by putting .strip() after the variables value.

# !!!! TEST COMMIT