# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/03/ 23:47 
"""

__author__ = "Rem"
import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        d = int(n)
        for maxiter in range(1, 64):
            if (d >> maxiter) <= 0:
                break
        for i in range(maxiter, 0, -1):
            test = int(math.pow(d, (1 / i)))
            if test == 1:
                continue
            ans = 1
            for j in range(i):
                ans *= test
                ans += 1
                if ans == d:
                    return str(test)
                if ans > d:
                    break
            # print("test", test)
            # print("ans",ans)
            # print()
            if ans == d:
                return str(test)
        return str(d - 1)


s = Solution()
print(s.smallestGoodBase("3"))
print(s.smallestGoodBase("4"))
print(s.smallestGoodBase("13"))
print(s.smallestGoodBase("1111"))
print(s.smallestGoodBase("1000000000000"))
print(s.smallestGoodBase(999*999 + 999 + 1))
print(s.smallestGoodBase(999*999*999 + 999*999 + 999 + 1))
for base in range(3, 80):
    for pow in range(2, 10):
        test_num = 1
        for j in range(pow):
            test_num *= base
            test_num += 1
        ans = s.smallestGoodBase(test_num)
        if int(ans) != base:
            print(base, pow, test_num, ans)
