class Bike(object):
    def __init__(self, price, max_speed=0, miles=7):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print 'Riding'
        self.miles += 10
        return self
    def reverse(self):
        print 'reversing'
        if self.miles >= 5:
            self.miles -=5
        else:
            self.miles = 0
        return self
red = Bike(100, 40, 30)
blue = Bike(200, 45, 0)
green = Bike(80, 25, 56)

red.ride().ride().ride().reverse().displayInfo()
blue.ride().ride().reverse().reverse().displayInfo()
green.reverse().reverse().reverse().displayInfo()
