class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		print "Creating Bike"
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	
	def displayinfo(self):
		print "Price", self.price
		print "Max Speed", self.max_speed
		print "Current Mileage", self.miles
		return self

	def ride(self, m=1):
		self.miles += 10 * m
		print "They see my Riding..."
		return self
		

	def reverse(self, m=1):	
		self.miles -= 5 * m
		if self.miles < 0:
			self.miles = 0
		print "They see me Rollin...backwards"
		return self

bike1 = Bike('$300', '40mph')

bike2 = Bike('$400', '45mph')

bike3 = Bike('$500', '50mph')


bike1.ride(3).reverse().displayinfo()

bike2.ride(2).reverse(2).displayinfo()

bike3.ride(0).reverse(3).displayinfo()

