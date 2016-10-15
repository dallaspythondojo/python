class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price < 10000:
			self.tax = "15%"
		else:
			self.tax = "12%"	

		self.display_all()

	def display_all(self):
		print "Price: ", self.price
		print "Speed: ", self.speed
		print "fuel: ", self.fuel
		print "mileage:", self.mileage
		print "Tax: ", self.tax
		print 

car1 = Car(20000, "80mph", "Full", "32mpg")	
car2 = Car(25000, "120mph", "Not Full", "18mpg")
car3 = Car(45000, "120mph", "kind of full", "28mpg")
car4 = Car(30000, "110mph", "Full", "34mpg")
car5 = Car(22000, "90mph", "Empty", "22mpg")
car6 = Car(9000, "80mph", "Empty", "24mpg")




