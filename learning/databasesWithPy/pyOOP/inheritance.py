class Account(object):

	def __init__(self,filepath):
		self.filepath=filepath
		with open(filepath,'r') as file:
			self.balance=int(file.read())

	def withdraw(self,amount):
		self.balance=self.balance-amount

	def deposit(self,amount):
		self.balance=self.balance+amount
	
	def commit(self):
	    	with open(self.filepath,'w') as file:
	    		file.write(str(self.balance))
	
class Checking(Account):
	"""this class inherites the Account class""" #this is the doc string
	type="checking"  #this is a class variable
	def __init__(self,filepath,fee):
		Account.__init__(self,filepath)
		self.fee=fee

	def transfer(self,amount):
		self.balance=self.balance-amount-self.fee

checking=Checking("balance.txt",5)
checking.deposit(100)
checking.transfer(200)
checking.commit()							
print(checking.__doc__)	