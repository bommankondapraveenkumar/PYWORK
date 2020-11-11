class Account:
	account_type='Basic'
	def __init__(self,name,balance):
		self.name=name
		self.balance=balance
	def deposit(self,value):
		self.balance+=value
	def withdraw(self,value):
		self.balance-=value
bank=Account('HSBC',1000)
