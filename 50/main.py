# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 21:02 
"""

__author__ = "Rem"


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1 / x
        ans = 1
        while n:
            if (n&1):
                ans *= x
            n = (n >> 1)
            x *= x
        return float(ans)


s = Solution()
print(s.myPow(1, 1000))

print(s.myPow(1.000000001, 2147483648))
print(s.myPow(2, 8))
