my_Dictionary = {
    "tony" : "Anthony Ramos",
    "howie" : "Howard the Duck"
}

username = input("Add a username: ")
name = input("what is the user's full name? ")

my_Dictionary[username] = name
print(my_Dictionary[username])

search = input("Search by username: ")
#useful if key doesnt exist otherwise python will crash
print(my_Dictionary.get(search, "Value not found"))