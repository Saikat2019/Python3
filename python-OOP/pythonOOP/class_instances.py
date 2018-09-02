class Employee:
	def __init__(self, first, second,pay):
		self.first = first
		self.second = second
		self.pay = pay
		self.email = first + '.' + second + '@gmail.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.second)

emp_1 = Employee('corey','schafer',20000)
emp_2 = Employee('saikat','mondal',10000)

#emp_1.email = 'saikat'

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())

print(Employee.fullname(emp_1))