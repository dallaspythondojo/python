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
        return self
    def ride(self, x=1):
        self.miles += 10 * x
        print 'Riding....'
        print self.miles
        return self
    def reverse(self):
        self.miles -= 5
        print 'reversing...'
        print self.miles
        if self.miles < 0:
            self.miles = 0

goldbike = Bike(900, 90)

goldbike.ride().ride().ride().reverse().displayInfo()
