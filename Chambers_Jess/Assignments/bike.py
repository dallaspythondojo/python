
class bike(object):
    def __init__(self, price, max_speed, miles):
        print 'New Bike'
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "Price is ", self.price, ", Max Speed is ", self.max_speed, "mph, Miles = ", self.miles,"."
        return self
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        if self.miles >5:
            self.miles -= 5
        print "Reversing"
        return self

mint_green = bike(75, 75, 0)

mint_green.ride().ride().ride().reverse().displayinfo()

greenish_blue = bike(80,80, 0)

greenish_blue.ride().ride().reverse().reverse().displayinfo()

yellow = bike(25, 25, 800)

yellow.reverse().reverse().displayinfo()
