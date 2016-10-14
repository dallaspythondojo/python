class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0
		if price > 10000:
			self.tax = .15
		else:
			self.tax = .12

	def displayinfo(self):
		print "Price: $" + str(self.price)
		print "Speed: " + str(self.speed) + "MPH"
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage) + " MPG"
		print "Tax: " + str(self.tax)

	def tax(self):
		if self.price > 10000:
			self.tax =15
		else:
			self.tax =12

car1 = Car(2000, 35,  "Full", 15)
car1.displayinfo()

car2 = Car(2000, 5, 'Not Full', 105)
car2.displayinfo()

car3 = Car(2000, 15, "Payday is still a week away", 95)
car3.displayinfo()

car4 = Car(2000, 25, "Full", 25)
car4.displayinfo()

car5 = Car(2000, 45, "Gas or Food, Gas or Food?", 25)
car5.displayinfo()

car6 = Car(2000000, 35, "Empty", 15)
car6.displayinfo() 