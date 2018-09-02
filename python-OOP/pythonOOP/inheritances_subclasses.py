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

class Developer(Employee):
		raise_amount = 1.10
		def __init__(self, first, second, pay, prog_lang=None):
			super().__init__(first, second, pay)
			if prog_lang == None :
				self.prog_lang = 'cpp'
			else :
				self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, second, pay, employees = None):
		super().__init__(first, second, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
			if emp not in self.employees :
				self.employees.append(emp)

	def remove_emp(self,emp):
			if emp not in self.employees :
				self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->  ',emp.fullname())

dev_1 = Developer('corey','schafer',20000,'python')
dev_2 = Developer('saikat','mondal',10000, 'js ')

#print(dev_2.email)
#dev_2.applyRaise()
#print(dev_2.pay)
#print(dev_2.prog_lang)

"""
hey its nice

   to learn oop in python,


 ''''''' i'm loving it  
"""

mgr_1 = Manager('sai','kat',100000,[dev_2])
mgr_1.add_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps()

print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))

print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))