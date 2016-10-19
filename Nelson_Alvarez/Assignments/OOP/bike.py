class bike(object):
	def __init__(self, price, max_speed, miles=0):
		print "Bike Time"
		self.price = price
		self.max_speed = max_speed
		self.miles = 0


	def displayinfo(self):
		print "Bike's Price:", self.price
		print "Max Speed:", self.max_speed
		print "Total Mileage", self.miles
		return self

	def ride(self, m=1):
		self.miles += 10 * m
		print "Crotchrocket is on the move!"
		return self


	def reverse(self, m=1):
		self.miles -= 5 * m
		if self.miles < 0:
			self.miles = 0
		print "back it up there buddy"
		return self 

bike1 = bike('$1000', '80mph')
bike2 = bike('$1500', '90mph')
bike3 = bike('$2000', '120mph')

bike1.ride(3).reverse().displayinfo()
bike2.ride(2).reverse(2).displayinfo()
bike3.reverse(3).displayinfo()