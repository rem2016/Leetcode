# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/21/ 21:39 
"""

__author__ = "Rem"


class TreeNode():
    def __init__(self, f, v):
        self.v = v
        self.f = f
        self.l = None
        self.r = None
        self.ln = 0
        self.rn = 0

    def __repr__(self):
        return str(self.v) + '{%s %s}' % (str(self.l), str(self.r))

    def findKth(self, k):
        if self.ln == k - 1:
            return self.v
        if self.ln > k - 1:
            return self.l.findKth(k)
        return self.r.findKth(k - 1 - self.ln)

    def insert(self, v):
        if v <= self.v:
            self.ln += 1
            if self.l is None:
                self.l = TreeNode(self, v)
            else:
                return self.l.insert(v)
        else:
            self.rn += 1
            if self.r is None:
                self.r = TreeNode(self, v)
            else:
                return self.r.insert(v)

    def popRightMost(self):
        if self.r:
            if not self.r.r:
                t = self.r.v
                self.r = 
                return t
            return self.r.popRightMost()
        t = self.v
        self.f.l = None
        return t

    def popLeftMost(self):
        if self.l:
            if not self.l.l:
                t = self.l.v
                self.l = None
                return t
            return self.l.popLeftMost()
        t = self.v
        self.f.r = None
        return t

    def remove(self, v):
        if self.v == v:
            if self.l:
                self.v = self.l.popRightMost()
                self.ln -= 1
            else:
                self.v = self.r.popLeftMost()
                self.rn -= 1
            return
        if self.v > v:
            self.ln -= 1
            return self.l.remove(v)
        else:
            self.rn -= 1
            return self.r.remove(v)

    @staticmethod
    def findMedian(root, n):
        if n & 1:
            return root.findKth((n + 1) // 2)
        return (root.findKth(n // 2) + root.findKth(n // 2 + 1)) / 2


class Solution:
    def medianSlidingWindow(self, nums, k):
        root = TreeNode(None, nums[0])
        for i in range(1, k):
            root.insert(nums[i])
        ans = []
        for i in range(k, len(nums)):
            print(root)
            ans.append(TreeNode.findMedian(root, k))
            root.remove(nums[i - k])
            root.insert(nums[i])
        print(root)
        ans.append(TreeNode.findMedian(root, k))
        return ans


def test(*args):
    s = Solution()
    print(s.medianSlidingWindow(*args))


test([1, 2, 3, 4, 5], 4)

