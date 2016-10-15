class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	
	def displayInfo(self):
		print(('Bike Info:\n'
			   'Price: {}\n'
			   'Maximum Speed: {}\n'
			   'Total Miles: {}').format(self.price, self.max_speed, self.miles))
		
		return self
	
	def ride(self):
		print('Riding...')
		self.miles += 10
		
		return self
		
	def reverse(self):
		print('Reversing...')
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		
		return self
	
street = Bike(1000, 45)
mountain = Bike(150, 30)
bmx = Bike(300, 20)

print('Street Bike')
print('bike').displayInfo().ride().ride().ride().reverse().displayInfo()
street.displayInfo().ride().ride().ride().reverse().displayInfo()

print('\nMountain Bike')
mountain.displayInfo().ride().ride().reverse().reverse().displayInfo()

print('\nBMX Bike')
bmx.displayInfo().reverse().reverse().reverse().displayInfo()

