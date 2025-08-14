class Employee:
    company="ITC"
    name="Priyanshu"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language="Python"
    def printlanguage(self):
        print(f"This is your:{self.language} language")



class Programmer(Employee,Coder):
    company="ITC infotech"
    name="Raj"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.company}")

a=Employee()
b=Programmer()

b.show()
b.printlanguage()
b.showlanguage()
