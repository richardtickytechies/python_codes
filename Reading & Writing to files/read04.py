funny=open("names.txt", "r")
for name in funny.readlines():
    print(name)
funny.close()