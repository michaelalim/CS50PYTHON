# Continuation of hello.py but trying to deep dive in functions
# In this we deep dive on the function: print()
# By default, function print() has a default parameter or argument of end="\n" which means next space
# It means that when print ends, it will automatically go to next line
# We could change that by rewriting this argument with end="" having no value for end
# NOTE that the default value for print is print(*objects, sep=" ", end='\n', file=sys.stdout, flush=False)

# ----------------------------------------------------------------------------------------------------------------------

# TEST

name = input("What is your name? ")
print("Hello,", end="")
print(name)

# In the above example, we could see that there's no space, that means two prints are not being separated by the default value of print() sep = " "
# That means that two prints are not separated but ended so maybe we could do end=" "

age = input("What is your age? ")
print("You are", end=" ")
print(age, end=" ")
print("years old")

# Works perfectly since we every end of print is a space " "

# ----------------------------------------------------------------------------------------------------------------------

# NOTE ON TERMS
# What we pass in on arguments are parameters
