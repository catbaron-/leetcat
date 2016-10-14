# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def readNumber(cur):
            if cur:
                return cur.next, cur.val
            else:
                return cur, 0

        c = 0
        r = ListNode(0)
        cur = r
        while l1 or l2 or c == 1:
            if c == 0 and not (l1 and l2):
                cur.next = l1 if l1 else l2
                return r.next
            v1, v2 = 0, 0
            if l1: l1, v1 = l1.next, l1.val
            if l2: l2, v2 = l2.next, l2.val
            sum = v1 + v2 + c
            c = 1 if sum > 9 else 0
            if sum > 9: sum = sum - 10
            cur.next = ListNode(sum)
            cur = cur.next
            
        return r.next