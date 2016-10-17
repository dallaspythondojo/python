class MathDojo(object):
	def __init__(self, sum = 0):
		self.sum = sum
	
	def add(self, arg1, *other_args):
		if type(arg1) == list or type(arg1) == tuple:
			for var in arg1:
				self.sum += var
		else:
			self.sum += arg1
		if other_args:
			for var in other_args:
				if type(var) == list or type(var) == tuple:
					for i in var:
						self.sum += i
				else:
					self.sum += var
		print self.sum
		return self

	def subtract(self, *args):
		adder = 0
		for var in args:
			if type(var) == list or type(var) == tuple:
				for i in var:
					adder += i
			else:
				adder += var
		self.sum -= adder
		print adder 
		print self.sum
		return self

	def result(self):
		print "The final value of the variable is {}".format(self.sum)
		return self



test = MathDojo()
test.add([1,4],3,4,[4,2]).subtract(3,2,[1,1]).result()