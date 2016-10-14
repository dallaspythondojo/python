class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
		self.displayInfo()

	def displayInfo(self):
		print "This bike costs ${}, can travel up to {}mph and and has {} miles on the clock".format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print "Riding..."
		self.miles += 10
		return self

	def reverse(self): 
		if (self.miles > 5):
			print "Reversing..."
			self.miles -= 5
		else:
			print "There are too few miles on this bike to reverse the odometer."
		return self
		
bike1 = Bike(200, 25)
bike2 = Bike(100, 10)
bike3 = Bike(850, 35)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



