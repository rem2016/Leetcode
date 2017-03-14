# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 21:18 
"""

__author__ = "Rem"
import collections

class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


s = Solution()
print(s.minWindow('ab', 'b'))
print(s.minWindow('81111111245', '81'))
print(s.minWindow('2', '1'))
print(s.minWindow('1', '1'))
print(s.minWindow('2123123', ''))
print(s.minWindow('123', '125'))
print(s.minWindow('612127831245555555555555555555556', '12346'))

