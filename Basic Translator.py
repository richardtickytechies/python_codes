def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"o"
        else:
            translation=translation+letter
    return translation
print("This translator turns all vowels into 'o'.")
print(translate(input("Enter a Phrase: ")))
# This is how a basic translator works.
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation+"O"
            else:
                translation=translation+"o"
        else:
            translation=translation+letter
    return translation
print("This translator turns all vowels into 'o'.")
print(translate(input("Enter a Phrase: ")))
# This is a more efficient version of it.
# Notice line 15.

