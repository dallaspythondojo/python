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
	
	def ride(self):
		print('Riding...')
		self.miles += 10
		
	def reverse(self):
		print('Reversing...')
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		
street = Bike(1000, 45)
mountain = Bike(150, 30)
bmx = Bike(300, 20)

print('Street Bike')
street.displayInfo()
street.ride()
street.ride()
street.ride()
street.reverse()
street.displayInfo()

print('\nMountain Bike')
mountain.displayInfo()
mountain.ride()
mountain.ride()
mountain.reverse()
mountain.reverse()
mountain.displayInfo()

print('\nBMX Bike')
bmx.displayInfo()
bmx.reverse()
bmx.reverse()
bmx.reverse()
bmx.displayInfo()

