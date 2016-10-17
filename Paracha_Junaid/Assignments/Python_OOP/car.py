class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = .12
		if self.price > 10000:
			self.tax = .15 
	def display_all(self):
		print "Price: $", self.price
		print "Speed: ", self.speed
		print "Fuel: ", self.fuel
		print "Mileage: ", self.mileage
		print "Tax: ", self.tax
		return self 
	

Car1 = Car(2000, 35 , 'Full', 15)
Car2 = Car(2000, 5 , 'Not Full', 105)
Car3 = Car(2000, 15 , 'Kind of Full', 95)
Car4 = Car(2000, 25 , 'Full', 25)
Car5 = Car(2000, 45 , 'Empty', 25)
Car6 = Car(2000000, 35 , 'Empty', 15)

Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()