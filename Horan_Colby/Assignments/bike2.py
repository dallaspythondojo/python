class Bike(object):
  	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0


	def displayinfo(self):
		print "Price: $" + str(self.price)
		print "Max Speed: " + str(self.max_speed) + "MPH"
		print "Total miles: " + str(self.miles) + 'miles'
		return self

	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -= 5
		return self

bike1 = Bike(200, 18)	
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike(120, 15)
bike2.ride().ride().reverse().reverse().displayinfo()


bike3 = Bike(30, 7)
bike3.reverse().reverse().reverse().displayinfo()
