class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price= price
		self.max_speed = max_speed
		self.miles = miles

	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self
	def ride(self):
		print 'Riding'
		self.miles +=10
		if self.miles <0:
			print('mileage has been corrupted')
		return self
	def reverse(self):
		print 'Reversing'
		self.miles-=5
		return self

bikeA= Bike(20,10,30)
bikeA.ride().ride().ride().displayinfo().reverse()

bikeB= Bike(10,10,10)
bikeB.ride().ride().reverse().reverse().displayinfo()

bikeC= Bike(50,50,50)
bikeC.reverse().reverse().reverse().displayinfo()




