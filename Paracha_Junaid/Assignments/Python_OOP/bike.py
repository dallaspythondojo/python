
class Bike(object):
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0
  def displayInfo(self):
   # - have this method display the bike's price, maximum speed, and the total miles.
    print "Price: $", self.price
    print "Max Speed:", self.max_speed
    print "Miles:", self.miles
    return self
  def ride(self):
   # - have it display "Riding" on the screen and increase the total miles ridden by 10
    print 'Riding'
    self.miles += 10
    return self
  def reverse(self):
    # have it display "Reversing" on the screen and decrease the total miles ridden by 5...
    print 'Reversing'
    self.miles -= 5
    return self
mybike = Bike(100, 50)
mybike.displayInfo()
mybike.ride().ride().ride().reverse().displayInfo()

# class Point(object):
#     def __init__(self,x = 0,y = 0):
#         print "Created a new point!"
#         self.x = x
#         self.y = y
#     def distance(self):
#         #Find distance from origin
#         return (self.x**2 + self.y**2) ** 0.5
# class Human(object):
#     def __init__(self):
#       print "New Human!!!"     #when we create a new human, we'll get this as an output
#     def taunt(self):
#       print "You want a piece of me?"