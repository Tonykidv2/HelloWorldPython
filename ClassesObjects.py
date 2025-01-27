from pydantic import BaseModel

class Person():
    name: str
    salary: int
    

    def info(self):
        return "A nobody"
    
class Developer(Person):
    langauge: str

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.langauge = language
        

    def info(self):
        return "Developer: " + self.name + ", salary: $" + str(self.salary) + ", Language: " + self.langauge
    
class Customer(Person):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return "Customer: " + self.name + ", Money to spend: $" + str(self.salary)
    
list = [Customer("Howard Duck", 300000), Customer("Matt Max", 30000), Developer("Anthony Ram", 60000, "C#"), Person()]

for item in list:
    print(item.info())

# person = {
#     "name" : "David Lumen",
#     "salary" : 300000,
# }

# # unpacking using **
# d = Person(**person)
# print(d.name + " : " + d.salary)
