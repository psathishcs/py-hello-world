import sys
import os
from org.hello.department import Department
print(sys.executable)
print(sys.version)


class Employee:
    """ A Simple Employee Class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return '{}.{}.@skylark.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Amsa', 'Parthasarathy')
emp_2 = Employee('Parthasarathy', 'Damodaran')
emp_3 = Employee('Sunil', 'Parthasarathy')
emp_4 = Employee('Sathish', 'Parthasarathy')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

print(emp_2.first)
print(emp_2.email)
print(emp_2.fullname)

print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)

print(emp_4.first)
print(emp_4.email)
print(emp_4.fullname)

node = [1, 2, 4, 64]

for i in node:
    print(i)

dep_1 = Department('Sales', 'Avadi')
print(dep_1.name)
print(dep_1.email)

dir_file_list = os.listdir('c:/')
print(dir_file_list)
