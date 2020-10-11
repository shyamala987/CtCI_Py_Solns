'''
Implement an algorithm to return the kth to last element of a singly linked list
'''
import linkedList
from linkedList import Node, LinkedList

class Solution:
    def findKthToLast(self, head, k):

        def findSize(head):
            size = 0
            while head is not None:
                size += 1
                head = head.next
            return size

        n = findSize(head)
        ctr = 0
        while head is not None:
            if (ctr == n-k):
                return head.val
            ctr += 1
            head = head.next

        return None

if __name__ == '__main__':
    ls = LinkedList()
    for i in [1, 3, 5, 2, 4, 2, 3, 5, 6]:
        node = Node(i)
        ls.addNode(node)
    s = Solution()
    k = int(input("Enter the value of K -\n"))
    ans = s.findKthToLast(ls.head, k)
    print("{} element from the last is {}".format(k, ans))