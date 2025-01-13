age = 20
price = 19.95

first_name = "Anthony"
is_online = True

# name = input("What is your Name? ")

# print("Hello " + name)
from datetime import datetime
birth_year = input("Enter your birth year: ")
current_year = datetime.now().year
age = current_year - int(birth_year)
# float()
# bool()
# str()
print(age)