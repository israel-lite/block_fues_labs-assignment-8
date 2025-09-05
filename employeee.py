class employee:
    def _init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{}' '{}'.format(self.first, self.last)
    

def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

emp_1 = employee('corey', 'scafer', 50000)
emp_2 = employee('test', 'user', 60000)

# print(employee.__dict__)

emp_1.raise_amount = 1.05

print(employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)