class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}s pay is {}'.format(self.first, self.last, self.pay)
    def applyRaise(self):
        self.pay = int(self.pay) * 1.15

emp_1 = Employee('Mok', 'Tan', '1000')
print(emp_1.applyRaise())
print(emp_1.fullname())
print(Employee.fullname(emp_1))
