import csv

class CSV_Parser:

    def parse_file(self, file_path):
        # store users in a list and return it
        user_list = []

        # open the csv file
        with open(file_path, "r") as file:

            # delimiter is the character that separates each column
            csv_reader = csv.reader(file, delimiter=",")
            
            # skip the headers with next() or a line counter
            next(csv_reader)

            for row in csv_reader: 
                # csv module automatically puts each column into a list: [name,email,balance]
                user = Customer(row[0], row[1], row[2])
                user_list.append(user)
         
        return user_list
    
class Customer: 

    name: str
    email: str
    balance: int

    index: int

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def info(self):
        return "Name: " + self.name + " Email: " + self.email + " Balance: " + '${:,.2f}'.format(int(self.balance))
        
userInput = input("Please input file path: ")
try:
    user_list = CSV_Parser().parse_file(userInput)
    for user in user_list:
        print(user.info())
except FileNotFoundError:
    print("file Not found")
except ZeroDivisionError:
    print("Stop Dividing by zero")
except:
    print("Something went wrong")