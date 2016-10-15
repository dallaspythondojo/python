class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0.15 if price > 10000 else 0.12
	
		self.display_all()
		
	def display_all(self):
		print(('Price: {}\n'
			   'Speed: {}mph\n'
			   'Fuel: {}\n'
			   'Mileage: {}mph\n'
			   'Tax: {}\n').format(self.price, self.speed, self.fuel, self.mileage, self.tax))

a = Car(2000, 35, 'Full', 15)
b = Car(2000, 5, 'Not Full', 105)
c = Car(2000, 15, 'Kind of Full', 95)
d = Car(2000, 25, 'Full', 25)
e = Car(2000, 45, 'Empty', 25)
f = Car(2000000, 35, 'Empty', 15)
