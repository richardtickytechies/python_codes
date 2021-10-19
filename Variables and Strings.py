change_name = "John"
change_age = "old"
print("There once was an old man named " + change_name + ", ")
print("he was very " + change_age + ", ")
change_name = "Tom"
# This would make the name on the bottom become Tom.
print("He really liked the name " + change_name + ", ")
print("but didn't like being " + change_age + ", ")
# This is a variable. By changing the text in quotation in line 8-9, you could replace the variables in lines 10-13
# Notes: Strings are Data that stores test. Just basic, plain text. You need "" to store strings
# You could also store numbers as data in python. Deciamls can be used too.
# There is also something known as a boolean value, which is just true or false.
number_age = 40
change_name = "John"
is_male = False
# Note that Booleans needs to be in capital.
print("This is a string.")
print("There is a break under this\nThere is a break above this.")
print("Oh look!\"A Quotation is here.")
print("This simply\creates a backslash.")
# \n means creating a break, similar to the <br> function.
# \" Will basically create a quotation in the middle of the text.
phrase = "Craftie"
print(phrase + " is cool!")
print(phrase.lower())
print(phrase.upper())
# This turns text into lowercase or uppercase.hfdhfdhrg
print(phrase.isupper())
print(phrase.islower())
# This checks if all the text is lowercase or uppercase.
print(phrase.upper().isupper())
# What this does is that it turns the text all into uppercase,
# then runs a test to see if all the text is uppercase or not.
print(len(phrase))
# This will show the amount of characters (including space) in the variable.
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])
# 𝐀𝐋𝐋 𝐈𝐍𝐃𝐄𝐗 𝐈𝐍 𝐒𝐓𝐑𝐈𝐍𝐆𝐒 𝐒𝐓𝐀𝐑𝐓 𝐖𝐈𝐓𝐇 𝟎
print("Index Section.")
double = "letter"
two = "Crafter Recruit"
print(double.index("t"))
#This would return the number of the text
# If there are more than one of the letter, it would return the location of the first one.
# You can also put text into the inside bracket.
print(two.index("Recruit"))
# This is going to show where the word Recruit starts in.
# Python will throw you an error if the requested letter does not exist in the variable's string.
print(two.replace("Recruit", "Team"))
# This would replace the word "Recruit" with the word "Team" in the Two variable.
