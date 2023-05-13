# We could put commas on our integer outputs which will make the output more readable for the users
# Example is we would like to make 1000 as 1,000, or 1000000 as 1,000,000 
# We could do it using a cryptic function :

x = float(input("First number: "))
y = float(input("Second number: "))

# We should try to input here something that will result to a 4-digit answer, example is 1 and 999

z = round(x + y)

# Output with no comma
print(end="" "The sum of x and y is: ")
print(z)

# Output modified with comma separators on thousands onwards
print(end="" "The sum of x and y with readable answer is ")
print(f"{z:,}")