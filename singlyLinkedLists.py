class Node(object):
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def printAllVals(self):
        node = self.head
        while node:
            print node.value
            node = node.next

    def addBack(self, value):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = Node(value)

    def addFront(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insertBefore(self,nextVal, value):
        curr_node = self.head
        node = Node(value)
        while curr_node:
            if curr_node.next.value == nextVal:
                nextVal = curr_node.next
                node.next = nextVal
                curr_node.next = node
                return
            else:
                curr_node = curr_node.next

    def insertAfter(self, prev_val, value):
        curr_node = self.head
        # 1. Create new node &
    	# 2. Put in the data
        new_node = Node(value)
        while curr_node:
            if prev_val == curr_node.value:
                # 3. Make next of new Node as next of prev_node
                new_node.next = curr_node.next
                # 4. make next of prev_node as new_node
                curr_node.next = new_node
                return
            else:
                # 5. contiune to next node
                curr_node = curr_node.next
    def removeNode(self, value):
        curr_node = self.head
        if curr_node.next.value == value:
            removed_node = curr_node.next
            curr_node.next = removed_node.next
            return

    def reverseList(self):
        prev_node = None
        curr_node = self.head
        while curr_node:
            next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next
        self.head = prev_node



my_list = SinglyLinkedList()
my_list.head = Node('Alice')
my_list.head.next = Node('Chad')
my_list.head.next.next = Node('Debra')
# print "Printing all values:"
# my_list.printAllVals() # print all values
#
# print "Adding a node in front of the list"
# my_list.addFront('Lata')
# my_list.printAllVals()
#
# print "Adding a node in the end of the list "
# my_list.addBack('Sara')
# my_list.printAllVals()
#
# print "Insert before: "
# my_list.insertBefore('Chad','Bob')
# my_list.printAllVals()
#
# print "Insert after: "
# my_list.insertAfter('Debra','Bob')
# my_list.printAllVals()
#
# print "Remove node:"
# my_list.removeNode('Chad')
# my_list.printAllVals()
#
print "Reverese a list:"
my_list.reverseList()
my_list.printAllVals()
