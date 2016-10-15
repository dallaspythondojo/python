class SinglyLinkedList(object):
    def __init__(self):
        self.head= None
    def PrintAllVals(self):
        runner = self.head
        while(runner):
           print(runner.val)
           runner=runner.next
    def AddBack(self, val):
        runner = self.head
        while(runner.next):
           runner=runner.next
        runner.next= Node(val)
    def AddFront(self, val):
        temp = self.head
        self.head=Node(val)
        self.head.next= temp
    def InsertBefore(self, nextVal, val):
        runner = self.head
        while(runner.next.val != nextVal):
            runner=runner.next
        temp = runner.next
        runner.next = Node(val)
        runner.next.next = temp
    def InsertAfter(self, preVal, val):
        runner= self.head
        while(runner.val != preVal):
            runner=runner.next
        temp= runner.next
        runner.next = Node(val)
        runner.next.next = temp
    def RemoveNode(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        runner=list.head
        while(runner.next.val != val):
            runner=runner.next
        runner.next = runner.next.next
    def ReverseList(self):
        previous=None
        runner=self.head
        next=runner.next
        while runner:
            runner.next=previous
            previous=runner
            runner=next
            if not runner.next:
                runner.next=previous
                break
            next=runner.next
        self.head=runner



class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.head.next.next.next = Node('Evan')


# print "Print All Vals: "
# list.PrintAllVals() #WORKS!
#
# print "Add Back: "
# list.AddBack('Evan')
# list.PrintAllVals() #WORKS!

# print "Add Front: "
# list.AddFront('Amy')
# list.PrintAllVals() #WORKS!

# print "Insert Before: "
# list.InsertBefore("Chad", "Evan")
# list.PrintAllVals() #WORKS!

# print "Insert After: "
# list.InsertAfter("Alice", "Ben")
# list.PrintAllVals() #WORKS!

# print "Remove Node: "
# list.RemoveNode('Alice')
# list.PrintAllVals() #WORKS!

print "Reverse List: "
list.ReverseList()
list.PrintAllVals() #WORKS!
