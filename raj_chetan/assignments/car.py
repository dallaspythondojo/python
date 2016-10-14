class Car(object):
	def __init__(self, price, speed, fuel, milage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.milage = milage
		if self.price > 10000:
			self.tax = 15
		else:
			self.tax = 12
		self.displayAll()

	def displayAll(self):
		print "This car has a price of ${}, a top speed of {}mph, has a tank that is {}, gets {}mpg, and has a tax rate of {}%".format(self.price, self.speed, self.fuel, self.price, self.tax)

car1 = Car(2000,35,'full',15)
car2 = Car(2000,5,'not full', 105)
car3 = Car(2000,15,'kinda full',95)
car4 = Car(2000,25,'full',25)
car5 = Car(2000,45,'empty',25)
car6 = Car(2000000,35,'empty',15)