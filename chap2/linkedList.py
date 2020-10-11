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