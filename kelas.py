class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
print "==================="
emp1.age = 7
emp1.age =8
#del emp1.age
print hasattr(emp1,'age')
print hasattr(emp1,'empCount')
print getattr(emp1,'age')
print setattr(emp1,'age', 8)
print delattr(emp1,'age')
print emp1.__doc__
print emp1.name
print emp1.__module__
print emp1.__class__
print emp1.__dict__

