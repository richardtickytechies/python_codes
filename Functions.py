def sayhi():
    username=input("Please Enter your name: ")
    print("Hello, "+username)
# Everything that comes after the line above is part of the function.
# When you type in code inside a function, it will be indented. This will tell python that it belongs to the code.
# To write things outside, simply delete the indent.
sayhi()
# This is how to execute the function.
# When you name a function, it needs to be all lowercase, and it better have an underscore, although not compulsory.
# Parameters are information that are recieved by functions.
def printname(name):
    print("Hello, user "+name)
# This name in the function tag is a parameter.
# It works like a variable inside of the function
printname("Tommy")
# This would replace the 'name' in the function into Tommy.
printname("Beasty")
# The same with Beasty
def printname(name,age):
    print("Hello, "+name+", your age is "+age+("."))
printname("Jimmy","54")
# This is how to put more than one parameter into the function.
# You would also notice the number is in strings.
def printname(name,age):
    print("Hello, "+name+", your age is "+str(age)+("."))
printname("Jim",31)
# By converting the number into a string, you fixed the problem.

