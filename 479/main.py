# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/20/ 20:10 
"""

__author__ = "Rem"


from math import sqrt
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]
        def getPlindrome(s):
            temp = s
            while temp:
                s = s*10 + temp%10
                temp //= 10
            return s

        if n == 1:
            return 9
        max_num = 10 ** n
        ans = 0
        for pld_num in range(10**n - 3, 0, -1):
            try_num = getPlindrome(pld_num)
            for factor in range(max_num, max(int(sqrt(try_num)+0.99), pld_num+1), -1):
                if try_num % factor == 0:
                    ans = try_num % 1337
                    print(try_num, factor, try_num / factor)
                    break
            if ans:
                break
        return ans

s = Solution()
for i in range(1,9):
    print(s.largestPalindrome(i))
