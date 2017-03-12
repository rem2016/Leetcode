# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/12/ 10:54 
"""

__author__ = "Rem"


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def toString(self):
        s = str(self.val)
        if not self.left and not self.right:
            return s
        s += '(%s)(%s)' % (self.left.toString() if self.left else 'n', self.right.toString() if self.right else 'n')
        return s

    def __repr__(self):
        return self.toString()


class Solution(object):
    def construct_node(self, s, index):
        if len(s) == index:
            return None, 0
        flag_n = False
        num = 0
        for i in range(index, len(s)):
            c = s[i]
            if c == '-':
                flag_n = True
                continue
            if c.isdigit():
                num *= 10
                num += ord(c) - ord('0')
            if c == ')':
                if flag_n:
                    num = -num
                return TreeNode(num), i + 1
            if c == '(':
                break
        if flag_n:
            num = -num
        node = TreeNode(num)
        node.left, new_i = self.construct_node(s, i+1)

        if new_i >= len(s) or s[new_i] == ')':
            return node, new_i + 1
        if s[new_i] == '(':
            node.right, i = self.construct_node(s, new_i+1)
        return node, i+1

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        root, _ = self.construct_node(s, 0)
        return root


s = Solution()
print(s.str2tree("4(2(3)(1))(6(5))").toString())
print(s.str2tree("2(-3(-4(5(6)(7)))(9(10)))").toString())
print(s.str2tree("-4(-2)(-6))").toString())

