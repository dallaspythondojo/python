class Bike(object):
    def __init__(self, price, max_speed):
        print 'You have got yourself a brand new bike!'
        self.max_speed = max_speed
        self.price = price
        self.miles = 0
    def displayinfo(self):
        print 'Price: $', self.price
        print 'Max speed', self.max_speed
        print 'Miles driven', self.miles
    def ride(self, x=1):
        self.miles += 10 * x
        print 'Riding....'
        print self.miles
    def reverse(self):
        self.miles -= 5
        print 'reversing...'
        print self.miles
        if self.miles < 0:
            self.miles = 0

goldbike = Bike(900, 90)

goldbike.ride()
goldbike.ride()
goldbike.ride()
goldbike.reverse()
goldbike.displayinfo()

redbike = Bike(400, 25)

redbike.ride()
redbike.ride()
redbike.reverse()
redbike.reverse()
redbike.displayinfo()

greenbike = Bike(200, 105)

greenbike.reverse()
greenbike.reverse()
greenbike.reverse()
greenbike.displayinfo()
