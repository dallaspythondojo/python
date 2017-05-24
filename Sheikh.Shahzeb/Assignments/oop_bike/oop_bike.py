class Bike(object):
	def __init__(self, price, miles, max_speed):
		self.price=price
		self.miles=miles
		self.max_speed=max_speed

	def displayinfo(self):
		print self.price
		print self.miles
		print self.max_speed
	def ride(self):
		print 'riding'
		self.miles +=10
		if self.miles <0:
			print('miles have been corrupted')
	def reverse(self):
		print 'reversing'
		self.miles -=5
		if self.miles<0:
			print('miles have been corrupted')



a = Bike(20,10,30)
a.ride()
a.ride()
a.ride()
a.reverse()
a.displayinfo()

b = Bike(10,10,10)
b.ride()
b.ride()
b.reverse()
b.reverse()
b.displayinfo()


c = Bike(50,50,50)
c.reverse()
c.reverse()
c.reverse()
c.displayinfo()







