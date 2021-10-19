print(2**3)
# This is basically 2^3 which is 2 cubed.
# This is an exponent
def raisetopower(base,pow):
    result=1
    for index in range(pow):
        result=result*base
    return result

print(raisetopower(456,4))
# This is how to create a exponent function
def raisetopower(base,pow):
    result=1
    for index in range(pow):
        result=result*base
    return result
basenum=input("Enter the base number: ")
pownum=input("Enter the power: ")
print(raisetopower(int(basenum),int(pownum)))
# This is a much more advanced version of it.
# Here is how it basically goes:
# The code will store two numbers, base and pow
# the answer of the entire thing would be stored in result
# Now, the for loop says that it will loop through the range of numbers, for a pow number of times.
# They would then set the result as result x base
# Finally, it would return the result.

