class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, second,pay):
		self.first = first
		self.second = second
		self.pay = pay
		self.email = first + '.' + second + '@gmail.com'

		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}'.format(self.first,self.second)

	def applyRaise(self):
			self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('corey','schafer',20000)
emp_2 = Employee('saikat','mondal',10000)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#print(Employee.__dict__)
Employee.applyRaise(emp_1)