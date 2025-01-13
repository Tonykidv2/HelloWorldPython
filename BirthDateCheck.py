from datetime import datetime
birth_year = input("Enter your birth year: ")
current_year = datetime.now().year
age = current_year - int(birth_year)
# float()
# bool()
# str()
print(age)