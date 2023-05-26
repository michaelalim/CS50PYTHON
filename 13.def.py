# As there is the function "function" on Javascript to make your own function, there is also a way to create your own function on Python, and the is "def"
# In this, we will create a VERY basic function
# def, is short for the word "define"


def hello(to):
    print(f"Hello, {to}")


name = input("What's your name? ").strip().title()

hello(name)

# SO WHAT HAPPENS HERE?
# we are calling the function "hello()" with parameter (name), the function accepts one parameter which is in the def, named "to". The name being called on the callout on line 11 is being applied on the function "hello" on line 6 which is to and is using that call to apply what its supposed to do.
# Basically, the "name" and "to" are the same, it's just labeled name outside the function, while to inside the function
