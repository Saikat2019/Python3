class Employee:
	num_of_emps = 0
	raise_amount = 1.04
	def __init__(self, first, second):
		self.first = first
		self.second = second
		
	@property
	def email(self):
		return "{}.{}@email.com".format(self.first,self.second)

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.second)

	@fullname.setter
	def fullname(self,name):
		self.first , self.second = name.split(' ')
		
	@fullname.deleter
	def fullname(self):
		self.first = None
		self.second = None
		print('Deleted !')


emp_1 = Employee('saikat','mondal')
emp_2 = Employee('biju','mondal')

emp_1.fullname = 'kartic chandra'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname) 