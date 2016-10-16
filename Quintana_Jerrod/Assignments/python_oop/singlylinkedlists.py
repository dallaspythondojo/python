# Each funcition has extra if statements added accordingly if the while loop doesn't work if the funciton needs to do its thing on the first node, if what it's looking for isn't in the list, or if the list is empy
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def printAllVals(self):
        current = self.head
        while current != None:
            print current.val
            current = current.next
    def AddBack(self, val):
        current = self.head
        new = Node(val)
        if current == None:
            current =new
            return list
        while current.next != None:
            current = current.next
        current.next = new
    def AddFront(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
    def InsertBefore(self, nextVal, val):
        current = self.head
        previous = None
        new = Node(nextVal)
        if current == None:
            current = new
            return list
        if current.val == val:
            temp = current
            self.head = new
            new.next = temp
            return self
        while current != None:
            if current.val == val:
                new.next = current
                previous.next = new
                return self
            previous = current
            current = current.next
        new.next = current
        previous.next = new
    def InsertAfter(self, preVal, val):
        current = self.head
        new = Node(preVal)
        if current == None:
            current = new
            return list
        while current != None:
            if current.val == val:
                new.next = current.next
                current.next =new
                return self
            if current.next == None:
                current.next = new
                return self
            current = current.next
    def RemoveNode(self, val):
        current = self.head
        previous = current
        if current.val == val:
            self.head = self.head.next
            current.next = None
            return self
        while current != None:
            if current.val == val:
                new = current.next
                previous.next = new
                current.next = None
                return self
            previous = current
            current = current.next
        return self
    def ReverseList(self):
        newList = SinglyLinkedList()
        current = self.head
        length_counter = 0
        start = current
        if current == None:
            return 'Starting list is empty'
        while start != None:
            length_counter += 1
            start = start.next
        for i in range (length_counter):
            # if i == length_counter:
            newList.AddFront(current.val)
            current = current.next
        newList.printAllVals()
        return self
        #i've been trying to somehow turn the original list into the new list once this function is finished so it would return that, and I honestly have no clue how to do it.




class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
# list.printAllVals()
list.AddBack('Holley')
list.AddFront('Drake')
list.InsertBefore('Nick', 'Chad')
list.InsertAfter('Susan', 'smith')
list.RemoveNode('Alice')
list.ReverseList()
list.printAllVals()
