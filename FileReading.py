#This 'with' will make sure our file will close in the background 
#so other application can access file after this block of code is done
#  other call file.close() once you're done reading a file
with open("Files/user.txt", "w") as file:
    #w = write
    file.write("Hank Hill\nTony Stark\nDavie Lumen\nDwayn Johnson")

with open("Files/user.txt", "a") as file:
    #a = append
    file.write("\nBob Hope")

with open("Files/user.txt", "r") as file:
    #r = read
    for line in file:
        print(line)



