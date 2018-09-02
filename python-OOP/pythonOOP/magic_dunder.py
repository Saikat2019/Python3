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
			self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first,self.second,self.pay)

	def __str__(self):
		return "{}-{}".format(self.fullname(),self.email)

	def __add__(self,other):
		return self.pay +other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('saikat','mondal',50000)
emp_2 = Employee('biju','mondal',20000)

#print(emp_1)
#print(emp_1.__repr__())
#print(emp_1.__str__())

print(emp_1+emp_2)

print(len(emp_1))