import collections

class Underscore(object):
	def __init__(self):
		super(Underscore, self).__init__()
		
	def map(self, items, callback):
		mapped = []
		
		if not self.is_iterable(items):
			print('Can\'t map non-iterable item yet...returning None')
			return None
		
		for item in items:
			mapped.append(callback(item))
			
		return mapped
	
	# start needed for lambdas requiring multiplication,
	# referenced http://stackoverflow.com/questions/9108855/how-does-reduce-function-work 
	# after initial implementation
	def reduce(self, items, callback, start=0): 
		reduced = start
		
		if not self.is_iterable(items):
			print('Can\'t reduce non-iterable item yet...returning None')
			return None
		
		for item in items:
			reduced = callback(reduced, item)
			
		return reduced
	
	def find(self, items, callback, toFind):
		found = None
		
		if not self.is_iterable(items):
			print('Can\'t find non-iterable item yet...returning None')
			return None		
		
		for item in items:
			found = callback(item, toFind)
			
			if not found == None:
				return found
			
		return found
	
	def filter(self, items, callback):
		filtered = []
		
		if not self.is_iterable(items):
			print('Can\'t filter non-iterable item yet...returning None')
			return None
		
		for item in items:
			if callback(item):
				filtered.append(item)
			
		return filtered
	
	def reject(self):
		accepted = []
		
		if not self.is_iterable(items):
			print('Can\'t filter non-iterable item yet...returning None')
			return None
		
		for item in items:
			if not callback(item) == None:
				accepted.append(item)
				
		return accepted
	
	def is_iterable(self, arg):
		if isinstance(arg, collections.Iterable):
			return True
		
		return False
	
# Simple tests for Underscore method implementations
_ = Underscore()

map_list = [1,2,3,4,5,6]
squared_list = _.map(map_list, lambda val: val ** 2)
print('Map() -> Squared values in {}: {}'.format(map_list, squared_list))

reduce_list = [1,2,3,4,5,6]
summed_list_value = _.reduce(reduce_list, lambda x, y: x + y)
print('Reduce() -> Summed values in {}: {}'.format(reduce_list, summed_list_value))

find_list = [1,2,3,4,5,6]
toFind = 5
found_value = _.find(find_list, lambda val, toFind: val if (val == toFind) else None, toFind)
print('Find() -> Find {} in values {}: {}'.format(toFind, find_list, found_value))

filter_list = [1,2,3,4,5,6]
evens = _.filter(filter_list, lambda val: val if (val % 2 == 0) else None)
print('Filter() -> Filtered evens in {}: {}'.format(filter_list, evens))

reject_list = [1,2,3,4,5,6]
# reject evens
accepted_list = _.filter(reject_list, lambda val: val if not (val % 2 == 0) else None)
print('Reject() -> Rejected evens in {}: {}'.format(reject_list, accepted_list))


	
