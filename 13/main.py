# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/11/ 11:30 
"""

__author__ = "Rem"


class Solution(object):
    def __init__(self):
        self.map = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'L': 50, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        temp, times = 0, 0
        for i in range(len(s)):
            v = self.map[s[i]]
            if v == 5:
                print(temp, times)
            if v == temp:
                times += 1
            elif v > temp:
                ans += - temp * times
                temp = v
                times = 1
            elif v < temp:
                ans += temp * times
                temp = v
                times = 1
        ans += temp * times

        return ans


s = Solution()
print(s.romanToInt("CDXXIV"))