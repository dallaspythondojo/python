class bike(object):
    def __init__ (self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print 'The bike cost {} has a max speed of {} and has driven {} miles.'.format(self.price, self.max_speed, self.miles)
        return self
    def ride(self, x = 1):
        self.miles += 10*x
        print 'riding'
        return self
    def reverse(self, x = 1):
        print 'reversing'
        self.miles -= 5*x
        if self.miles < 0:
            self.miles = 0
        return self



bike1 = bike(200, '25mph')
bike2 = bike(120, '20mph')
bike3 = bike(250, '30mph')


bike1.ride(3).reverse().displayinfo()
bike2.ride(2).reverse(2).displayinfo()
bike3.reverse(3).displayinfo()
