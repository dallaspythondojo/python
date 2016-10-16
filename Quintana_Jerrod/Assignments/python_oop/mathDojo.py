import collections
class MathDojo(object):
    def __init__(self, num):
        self.num = num
    def display(self):
        print self.num
        return self
    def add(self, *val):
        total = 0
        if isinstance(val, collections.Iterable):
            #this line is necessary because with the * infront of val, even if it's only one varible, it returns a tuple, so like a list it has a length and must be iterated through, even if there's only one value
            for i in range(len(val)):
                #this first for loop iterates through the tuple, or the entire *val given, even if it's only a single integer, we have to access it first
                if isinstance(val[i], collections.Iterable):
                    #this loop says that if we can iterate through whatever index of the tuple we're on, ex: whether that index of the tuple is an integer or a list. If we can iterate through it we do it below
                    sum = 0
                    for x in range (len(val[i])):
                        sum += val[i][x]
                        # if the index of the tuple we're on is a lsit, this will iterate through it and add each value to sum so it can be added to the total later
                    total += sum
                else:
                    total += val[i]
                    #this else is if the index of the tuple we're on is just a single integer instead of a list
        else:
            print "add didn't work"
        self.num += total
        return self
    def subtract(self, *val):
        total = 0
        if isinstance(val, collections.Iterable):
            for i in range(len(val)):
                if isinstance(val[i], collections.Iterable):
                    sum = 0
                    for x in range (len(val[i])):
                        sum += val[i][x]
                    total += sum
                else:
                    total += val[i]
        else:
            print "subtract didn't work"
        self.num -= total
        return self
md = MathDojo(0)
md.add(2,3).add(5).subtract(2,1).display()
md.add([9,4], 4, [1,1,1]).display()
md.subtract([2], 1, [5,5]).display()

#Look below for answer sheet, done much more elegantly

# PART III
# Make any needed changes in MathDojo in order to support tuples of
# values in addition to lists and singletons.

# class MathDojo2(object):
# 	def __init__(self):
# 		self.summed = 0
# 	def add(self, *args, **kwargs):
# 		for x in args:
# 			if type(x) is list:
# 				for i in x:
# 					self.summed = self.summed + i
# 		for x in args:
# 			if type(x) is int:
# 				self.summed = self.summed + x
# 		return self
# 	def subtract(self, *args, **kwargs):
# 		for x in args:
# 			if type(x) is list:
# 				for i in x:
# 					self.summed -= i
# 		for x in args:
# 			if type(x) is int:
# 				self.summed = self.summed - x
# 		return self
# 	def result(self):
# 		print(self.summed)
#
# md2 = MathDojo2()
# md2.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
#
# # PART III
# # Make any needed changes in MathDojo in order to support tuples of
# # values in addition to lists and singletons.

# class MathDojo3(object):
# 	def __init__(self):
# 		self.summed = 0
# 	def add(self, *args, **kwargs):
# 		for x in args:
# 			if type(x) is int:
# 				self.summed = self.summed + x
# 		for x in args:
# 			if type(x) is list:
# 				for i in x:
# 					self.summed = self.summed + i
# 		for x in args:
# 			if type(x) is tuple:
# 				for i in x:
# 					self.summed += i
# 		return self
# 	def subtract(self, *args, **kwargs):
# 		for x in args:
# 			if type(x) is int:
# 				self.summed = self.summed - x
# 		for x in args:
# 			if type(x) is list:
# 				for i in x:
# 					self.summed -= i
# 		for x in args:
# 			if type(x) is tuple:
# 				for i in x:
# 					self.summed -= i
# 		return self
# 	def result(self):
# 		print(self.summed)
#
# md3 = MathDojo3()
# tup = (1,3,4)
# md3.add(tup, [1,2,3], 9, 8, 10).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
