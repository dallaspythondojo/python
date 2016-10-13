class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price
        print self.max_speed 
        print self.miles

    def ride(self):
        print 'Riding dirty...'
        self.miles += 10

    def reverse(self):
        print 'Reversing...'
        self.miles -= 5


a = Bike(200, 60, 40)
b = Bike(400, 30, 20)
c = Bike(1000, 10, 60)

a.ride()
a.ride()
a.ride()
a.reverse()
a.displayInfo()

b.ride()
b.ride()
b.reverse()
b.reverse()
b.displayInfo()

c.reverse()
c.reverse()
c.reverse()
c.displayInfo()