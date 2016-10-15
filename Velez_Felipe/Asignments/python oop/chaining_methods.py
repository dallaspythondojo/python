class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print self.price, self.max_speed, self.miles
		return self

	def ride(self):
		self.miles +=10
		print "Riding", "Total miles ridden:",self.miles
		return self

	def reverse(self):
		self.miles -=5
		if self.miles < 0:
			self.miles = 0
		print "Reversing"
		return self

bike1 = Bike(200, 20)
bike2=Bike(450,10)
bike3 = Bike(100, 30)

bike1.displayinfo()

bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
