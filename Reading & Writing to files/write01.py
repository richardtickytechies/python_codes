funny=open("add_to_file01.txt", "a")
# This adds things at the end of the file
funny.write("Tommy gon gon")
# WARNING: Adding to files could mess up the program because if you run it again, it is going to print double the text.
funny.write("\nTommy gon gon")
# This will cause it to go to the next line because of the \n function
funny.close()
#TIP: MAKE SURE TO DELETE EVERYTHING IN add_to_file01.txt BEFORE RUNNING!!
