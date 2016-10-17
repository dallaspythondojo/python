import collections

class MathDojo(object):
	def __init__(self):
		super(MathDojo, self).__init__()
		
		self.result = 0
		
	def add(self, arg, *varargs):
		# add arg to result
		if self.is_iterable(arg): # handles adding each item if arg is iterable object
			for value in arg:
				self.result += value
		else: 
			self.result += arg
		
		# add varargs to result
		for vararg in varargs:
			if self.is_iterable(vararg): # handle if varargs contains iterable objects
				for value in vararg:
					self.result += value
			else:
				self.result += vararg
		
		return self
	
	def subtract(self, arg, *varargs):
		# subtract arg to result
		if self.is_iterable(arg): # handles subtracting each item if arg is iterable object
			for value in arg:
				self.result -= value
		else: 
			self.result -= arg
		
		# subtract varargs to result
		for vararg in varargs:
			if self.is_iterable(vararg): # handle if varargs contains iterable objects
				for value in vararg:
					self.result -= value
			else:
				self.result -= vararg
		
		return self
	
	def is_iterable(self, arg):
		if isinstance(arg, collections.Iterable):
			return True
		
		return False

md = MathDojo()
print('MathDojo result: {}'.format(md.result))

md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3])
print('MathDojo result: {}'.format(md.result))

md2 = MathDojo()
print('MathDojo result: {}'.format(md2.result))

md2.add(2).add(2, 5).subtract(3, 2).result
print('MathDojo result: {}'.format(md2.result))
