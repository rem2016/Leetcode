# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 19:14 
"""

__author__ = "Rem"


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        ans = []
        node = self
        while node:
            ans.append(str(node.val))
            node = node.next
        return ' '.join(ans)
    def build(self, list):
        node = self
        for i in list[:-1]:
            node.val = i
            node.next = ListNode(0)
            node = node.next
        node.val = list[-1]
        return



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next
        n = length - n
        if n == 0:
            return head.next
        node = head
        i = 0
        while i + 1 != n:
            i += 1
            node = node.next
        node.next = node.next.next
        return head


a = ListNode(0)
a.build([1,2,3,4,6])
s = Solution()
print(s.removeNthFromEnd(a, 2))
a.build([1,2,3,4,6])
print(s.removeNthFromEnd(a, 1))
a.build([1,2,3,4,6])
print(s.removeNthFromEnd(a, 5))
