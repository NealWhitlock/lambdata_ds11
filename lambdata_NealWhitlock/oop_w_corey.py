class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04 # Class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{0.first} {0.last}'.format(self)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # Works with class instead of instance
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or if day.weekday() == 6:
            return False
        return True

# print(Employee.num_of_emps)

emp_1 = Employee('Neal', 'Whitlock', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))


# emp_str_1 = 'John-Dope-70000'
# emp_str_2 = 'Jane-Doe-90000'
# emp_str_3 = 'Rob-Smith-40000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.num_of_emps)

Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)