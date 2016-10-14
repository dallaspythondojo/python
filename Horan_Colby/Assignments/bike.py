class Bike(object):
  	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0


	def displayinfo(self):
		print "Price: $" + str(self.price)
		print "Max Speed: " + str(self.max_speed) + "MPH"
		print "Total miles: " + str(self.miles) + 'miles'


	def ride(self):
		print "Riding"
		self.miles += 10

	def reverse(self):
		print "Reversing"
		self.miles -= 5


bike1 = Bike(200, 18)	
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(120, 15)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(30, 7)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()

# Make sure it doesn't have negative miles by setting up an if statement to only do negative miles if it has over 5 miles