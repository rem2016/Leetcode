# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 21:11 
"""

__author__ = "Rem"


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ('(', '[', '{')
        right = (')', ']', '}')
        for sign in s:
            if sign in left:
                stack.append(sign)
            else:
                if stack:
                    temp = stack.pop()
                else:
                    return False
                if left.index(temp) != right.index(sign):
                    return False
        return len(stack) == 0
