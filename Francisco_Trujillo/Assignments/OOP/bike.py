class Bike(object):
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    
    def displayInfo(self):
        print(self.miles)
        print(self.price)
        print(self.max_speed)
        return self
    
    def ride(self):
        print('Riding')
        self.miles += 10
        return self

    def reverse(self, miles = 1):
        print('Reversing')
        if miles >= 5:
            self.miles-=5
        else: print('There is no such a thing and negative miles')
        return self


print('First Instance')
bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

print('Second Instance')
bike2=Bike(200,'25mph')
bike2.ride().ride().reverse().displayInfo()

print('Third instance')
bike3 = Bike(200, '25mph')
bike3.reverse().reverse().reverse().displayInfo()
