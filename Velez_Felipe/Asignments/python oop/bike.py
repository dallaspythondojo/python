class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print self.price, self.max_speed, self.miles
		

	def ride(self):
		self.miles +=10
		print "Riding", "Total miles ridden:",self.miles
		

	def reverse(self):
		self.miles -=5
		if self.miles < 0:
			self.miles = 0
		print "Reversing"
		

bike1 = Bike(200, 20)
bike2=Bike(450,10)
bike3 = Bike(100, 30)

bike1.displayinfo()
bike1.displayinfo()
bike1.displayinfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()
bike3.reverse()
bike3.reverse()
bike.reverse()
bike.displayinfo()

