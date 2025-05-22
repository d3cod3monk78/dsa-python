class CreditCard:
	def __init__(self, customer, bank, account, balance, limit):
		self.__customer = customer
		self.__bank = bank
		self.__account = account
		self.__balance = balance
		self.__limit = limit

	@property
	def customer(self):
		return self.__customer

	@property
	def bank(self):
		return self.__bank

	@property
	def account(self):
		return self.__account

	@property
	def balance(self):
		return self.__balance

	@property
	def limit(self):
		return self.__limit

	def charge(self, price):
		if price + self.__balance > self.__limit:
			return False
		else:
			self.__balance = self.__balance + price
			return True

	def make_payment(self, amount):
		self.__balance = self.__balance - amount


card = CreditCard('Marlon', 'Sampath', '6542456', 18000, 15000)