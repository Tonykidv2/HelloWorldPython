from HelperFunctions import is_number

grade = input("Enter student score: ")

while(not is_number(grade)):
    grade = input("Please enter number input: ")

num_grade = int(grade)

if (num_grade >= 90):
    print('A')
elif (num_grade >= 80 and num_grade <= 89):
    print('B')
elif (num_grade >= 70 and num_grade <= 79):
    print('C')
elif (num_grade >= 60 and num_grade <= 69):
    print('D')
else:
    print('Failure')