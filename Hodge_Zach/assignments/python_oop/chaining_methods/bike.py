class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price: " + str(self.price)
        print "Max Speed: " + str(self.max_speed)
        print "Miles: " + str(self.miles)
        return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        self.miles -= 5;
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(100, "20mph")

bike1.ride().ride().ride().reverse().displayinfo()

bike2.ride().ride().reverse().reverse().displayinfo()

bike3.reverse().reverse().reverse().displayinfo()
