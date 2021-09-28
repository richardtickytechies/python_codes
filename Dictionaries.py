monthconvert={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    1:"One"
}
# Remember to put commas after each one.
# Inside the dictionary is the key-value-pair
# Whenever you write a dictionary, make sure its in curly brackets.
# This would turn basic three digit month names into full month names.
# NEVER use duplicate names for dictionaries.
print(monthconvert["Jun"])
# This is how to access one of the items.
print(monthconvert.get("Jan"))
# This is another method, but more advanced
print(monthconvert.get("Ja","Not a Valid Key."))
# What this does is that if it doesn't find the dictionary, it would go with the next one, which is the default one
print(monthconvert[1])
print(monthconvert.get(1))
# Numbers also work.

