'''
Write code to remove duplicates from an unsorted linked list
Follow up: How would this change if a temp buffer is not allowed?
i/p
1 -> 3 -> 5 -> 2 -> 4 -> 2 -> 3 -> 5 -> 6

o/p
1 -> 6
'''
import linkedList
from linkedList import Node, LinkedList

class Solution:
    def __init__(self):
        self.cache = {}

    def removeDups(self, head):
        curr = head
        dummy = Node(0)
        while curr is not None:
            if curr.val not in self.cache:
                self.cache[curr.val] = True
                dummy.next = curr
                dummy = dummy.next

            curr = curr.next
        return head

if __name__ == '__main__':
    ls = LinkedList()
    for i in [1, 3, 5, 2, 4, 2, 3, 5, 6]:
        node = Node(i)
        ls.addNode(node)
    ls.getValues()
    s = Solution()
    res = s.removeDups(ls.head)
    while res is not None:
        print(str(res.val) + ' -> ', end="")
        res = res.next
    print("None\n")