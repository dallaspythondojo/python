class Node(object):
	def __init__(self, value):
		self.val = value
		self.next = None


class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def traverse(self):
		runner = self.head
		while (runner != None):
			print runner.val
			runner = runner.next

	def AddBack(self, addval):
		node_to_add = Node(addval)
		runner = self.head
		while (runner.next != None):
			runner = runner.next
		runner.next = node_to_add
		self.traverse()

	def AddFront(self, addval):
		node_to_add = Node(addval)
		temp_head_holder = self.head
		self.head = node_to_add
		self.head.next = temp_head_holder
		self.traverse()

	def InsertBefore(self, addBefore, addval):
		node_to_add = Node(addval)
		runner = self.head
		while (runner != None):
			if runner.val == addBefore:
				last_node.next = node_to_add
				node_to_add.next = runner
			last_node = runner
			runner = runner.next
		self.traverse()

	def InsertAfter(self, nextVal, addval):
		node_to_add = Node(addval)
		runner = self.head
		while (runner != None):
			if runner.val == nextVal:
				temp_next = runner.next
				runner.next = node_to_add
				node_to_add.next = temp_next
			runner = runner.next
		self.traverse()



book = SinglyLinkedList()
book.head = Node('Alice')
book.head.next = Node('Chad')
book.head.next.next = Node('Debra')
