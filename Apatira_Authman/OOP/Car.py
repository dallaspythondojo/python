class Car(object):
    def __init__(self, price, speed, mileage):
        self.price = price
        self.speed = speed
        self.milege = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .10
    def displayAll(self, fuel):
        print 'Price :' + str(self.price)
        print 'Speed :' + str(self.speed)
        print 'Fuel :' + str(fuel)
        print 'Mileage :' + str(self.milege) + 'mpg'
        print 'Tax :' + str(self.tax)


a = Car(2500,110,25)
a.displayAll('Full')

b = Car(40000,160,28)
b.displayAll('Empty')

c = Car(100000,210,15)
c.displayAll('At the car wash')

d = Car(100,10,15)
c.displayAll('Stuck in traffic')

e = Car(106000,20,45)
c.displayAll('On the side of the road')

f = Car(100000,210,15)
c.displayAll('Riding dirty')
