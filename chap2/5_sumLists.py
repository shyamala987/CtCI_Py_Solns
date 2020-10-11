'''
Given two numbers represented by a linked list, the digits of the numbers are stored in reverse order. Wrute a function that adds the numbers and stores the result as a linked list
Follow up: What if the numbers are stored in forward order?
'''

import linkedList
from linkedList import Node, LinkedList

def sumReverseOrder(l1, l2):
    carry = 0
    dummy = Node(0)
    ans = dummy
    while l1 and l2:
        r = (l1.val+l2.val+carry)%10
        dummy.next = Node(r)
        carry = (l1.val+l2.val+carry)/10
        dummy = dummy.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        r = (l1.val + carry) % 10
        dummy.next = Node(r)
        carry = (l1.val + carry) / 10
        dummy = dummy.next
        l1 = l1.next

    while l2:
        r = (l2.val + carry) % 10
        dummy.next = Node(r)
        carry = (l2.val + carry) / 10
        dummy = dummy.next
        l2 = l2.next


    return ans.next


def sumForwardOrder(l1, l2):
    '''
    5 1 => 1 5
    6 7 8 => 8 7 6
    3 reversals
    stack same space as 3 reversals except we can do it without modifying the ll
    0 5 1
    6 7 8

    6 12 9

    9 9 9
    9 9 9
    18 18 18
    19 9 8
    1/ pad zeros at front of shortler list
    2/ add and dont propagate carry
    3/ check if next.val >= 10, then add 1 to curr.val and check next.val to next.val % 10
    :param l1:
    :param l2:
    :return:
    '''

    n1, n2 = l1.size(), l2.size()
    if n1 < n2:
        for i in range(n2-n1):
            l1.addToFront(0)
    elif n1 > n2:
        for i in range(n1-n2):
            l2.addToFront(0)
    print("Both lists are now equal")
    l1, l2 = l1.head, l2.head
    dummy = Node(0)
    first = dummy
    while l1 and l2:
        dummy.next = Node(l1.val+l2.val)
        dummy = dummy.next
        l1 = l1.next
        l2 = l2.next

    start = first.next
    print(start.val)
    final = Node(1) if start.val >= 10 else Node(0)
    start.val = start.val % 10 if start.val >= 10 else start.val
    answer = final
    while start is not None and start.next is not None:
        if start.next.val >= 10:
            start.val += 1
            start.next.val = start.next.val % 10
        final.next = start
        final = final.next
        start = start.next

    return answer.next if answer.val == 0 else answer

if __name__ == '__main__':
    ls1 = LinkedList()
    ls2 = LinkedList()
    for i in [9, 9, 7, 1, 6]:
        node = Node(i)
        ls1.addNode(node)
    for i in [9, 9, 5]:
        node = Node(i)
        ls2.addNode(node)

    #res = sumReverseOrder(ls1.head, ls2.head)
    res = sumForwardOrder(ls1, ls2)
    while res:
        print(str(res.val)+" -> ", end="")
        res = res.next

    print("None\n")