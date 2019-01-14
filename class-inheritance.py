class Employee: 
    raise_amount = 1.04
    def __init__(self, first,last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
            
class Developer(Employee):
    raise_amount = 5.34
    
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        #Employee.__init__(first, last, pay)
        
        self.programming_language = programming_language
        
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            
    def print_employee(self):
        for employee in self.employees:
            print("-->", employee.fullname())

#----------------------------------------------------

dev_1 = Developer("Core", "Sajal", 50000, "Python")
dev_2 = Developer("Abir", "Ahmed", 60000, "Java")
"""
print(dev_1.email)
print(dev_2.email)

dev1 = Developer("Karim", "Adnan", 4000)
print(dev1.email)"""

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

#print(dev_1.programming_language)

mag_1 = Manager("sUE", "sMIT", 80000, [dev_1])

#print(mag_1.email)

#mag_1.add_employee(dev_2)
#mag_1.remove_employee(dev_1)

#mag_1.print_employee()

print(isinstance(mag_1,Manager))
print(issubclass(Manager, Employee))