
class Bike(object):
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = miles
  def displayInfo(self):
   # - have this method display the bike's price, maximum speed, and the total miles.
    print "Price: $", self.price
    print "Max Speed:", self.max_speed
    print "Miles:", self.miles
  def ride(self,miles):
   # - have it display "Riding" on the screen and increase the total miles ridden by 10
    return self.miles + 10
  def reverse(self,miles):
    # have it display "Reversing" on the screen and decrease the total miles ridden by 5...
    return self.miles - 5
mybike = Bike(100, 50, 100)
print mybike.displayInfo()
print "Riding:", mybike.ride(mybike.miles)
print "Reversing:", mybike.reverse(mybike.miles)
print mybike

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