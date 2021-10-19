numgrid=[
    [1,2,3,],
    ["a","b","c"],
    [4,5,6],
    [0]
]
# So in this list, we have items itself as lists.
# This grid as 4 rows and 3 columns
print(numgrid[1][0])
# This is how to access specific items in the grid
# print(numgrid[index_of_row][index_of_column])
# This is how it works, remember, index starts with 0
# this is a 2D List, it basically means a list in a list.
for row in numgrid:
    print(row)
# This will print out each row in the numgrid
for row in numgrid:
    for col in row:
        print(col)
# This will give every item in the list in a seperate row.

