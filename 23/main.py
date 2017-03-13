# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/13/ 20:48 
"""

__author__ = "Rem"


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(lst):
        node = ListNode(lst[0])
        ans = node
        for v in lst[1:]:
            node.next = ListNode(v)
            node = node.next
        return ans

    def __repr__(self):
        s = []
        node = self
        while node is not None:
            s.append(str(node.val))
            node = node.next
        return ' '.join(s)




class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # count n
        n = 0
        for node in lists:
            while node != None:
                node = node.next
                n += 1
        k = len(lists)
        wei = 1
        while n >> wei != 0:
            wei += 1

        if k > 20 * wei:
            lst = []
            for node in lists:
                while node != None:
                    lst.append(node.val)
                    node = node.next
            lst.sort()
            root = None
            node = None
            for v in lst:
                if node == None:
                    root = ListNode(v)
                    node = root
                else:
                    node.next = ListNode(v)
                    node = node.next
            return root


        root = None
        cnode = None
        while True:
            minv, minindex = 2147483647, -1
            for index, node in enumerate(lists):
                if node is None:
                    continue
                if node.val <= minv:
                    minv, minindex = node.val, index
            if minindex == -1:
                break
            if cnode is None:
                root = ListNode(minv)
                cnode = root
            else:
                cnode.next = ListNode(minv)
                cnode = cnode.next
            lists[minindex] = lists[minindex].next
        return root


s = Solution()
a1 = ListNode.create([1,2,3,8,9])
a2 = ListNode.create([3,5,13,81,90])
a3 = ListNode.create([30,50,113,181,190])
print(s.mergeKLists([a1, a2, a3]))
print(s.mergeKLists([ListNode(i) for i in range(500)]))
