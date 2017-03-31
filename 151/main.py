# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/27/ 21:06 
"""

__author__ = "Rem"


class Solution(object):
    def reverse(self, s):
        t = s.split(' ')
        t.reverse()
        return ' '.join((x for x in t if x))

s = Solution()
print(s.reverse('the sky   is blue    '))
