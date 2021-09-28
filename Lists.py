listfriend=["Kevin","John","Tom","Will","Gorden","Ramsay"]
# You could also add booleans and numbers into the square brackets.
print(listfriend)
# This is how to print the list.
print(listfriend[0])
print(listfriend[1])
print(listfriend[2])
# This is how to mention specific items in the list, via index.
# Remember all index starts with a 0
print(listfriend[-1])
print(listfriend[-2])
print(listfriend[-3])
# If you give a negative value, it would start listing from the end.
print(listfriend[1:3])
# This would select everything between index 1 to index 3
print(listfriend[2:])
# This would select everything after index 2
listfriend[1]="Johnson"
print(listfriend)
# This would change the name in index 1 into Johnson.
numbers=[7,15,17,49,23,19,23]
list_alpha=["a","b","c","c","e","f","g","h","i","j","k","l",]
print(list_alpha)
# This is just an ordinary list, nothing unusual :)
list_alpha.extend(numbers)
print(list_alpha)
# This allows you to extend/combine two lists together.
numbers=[7,15,17,49,23,19,23]
list_alpha=["a","b","c","c","e","f","g","h","i","j","k","l",]
list_alpha.append("Mm")
print(list_alpha)
# This is how to adda item to the end of the list.
list_alpha=["a","b","c","c","e","f","g","h","i","j","k","l",]
list_alpha.insert(3,"break")
print(list_alpha)
# This is how to add a item into the middle of the list.
# The first digit is the index, of where you want to insert the item, the second is what you want to insert.
list_alpha=["a","b","c","e","f","g","h","i","j","k","l",]
list_alpha.remove("b")
print(list_alpha)
list_alpha.clear()
print(list_alpha)
# This is how to clear/remove specific or all items in a list.
list_alpha=["a","b","c","e","f","g","h","i","j","k","l",]
list_alpha.pop()
print(list_alpha)
# This removes the last element from the list.
list_alpha=["a","b","c","e","f","g","h","i","j","k","l",]
print(list_alpha.index("b"))
# This would show the index of the word you are looking for in the list.
list_alpha=["a","b","B","c","e","f","g","h","i","j","k","l",]
print(list_alpha.count("b"))
# This would count the amount of 'words' you put in the brackets. (it is case sensitive.
list_alpha=["d","a","B","x","e","f","k","h","i","n","w","l",]
list_alpha.sort()
print(list_alpha)
numbers=[75,135,17,49,255,139,23]
numbers.sort()
print(numbers)
# This will sort the letters, based on capitalization, and alphabetical order. It can also sort out numbers.
list_alpha=["a","b","c","e","f","g","h","i","j","k","l",]
list_alpha.reverse()
print(list_alpha)
# This would reverse the list
list_alpha=["a","b","c","e","f","g","h","i","j","k","l",]
list_alpha2=list_alpha.copy()
list_alpha2.remove("b")
print(list_alpha2)
print("The one above is list_alpha2")
print(list_alpha)
# This is how to copy lists. To show that it has worked, I removed the letter b from list_alpha2













