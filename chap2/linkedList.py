class Node:
    def __init__(self, val):
        self.val = int(val)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def getValues(self):
        print("Retrieving LS values")
        curr = self.head
        while curr is not None:
            print(str(curr.val) + ' -> ', end="")
            curr = curr.next
        print("None\n")

    '''
    1 -> 2 -> 3 -> 4
    4 -> 3 -> 2 -> 1
    '''
    def reverse(self):
        curr = self.head
        prev = None
        while curr.next is not None:
            nxt = curr.next
            nxt.next = curr
            curr.next = prev
            prev = curr
            curr = nxt
        return curr

    def size(self):
        curr = self.head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        return size

    def addToFront(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node