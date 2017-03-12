# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/12/ 10:44 
"""

__author__ = "Rem"


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) <= k:
            a = list(s)
            a.reverse()
            return ''.join(a)
        ans = []
        stack = []
        for i, c in enumerate(s):
            # k
            if (i // k) % 2 == 0:
                stack.insert(0, c)
            # 2k
            else:
                if i % k == 0:
                    ans.extend(stack)
                    stack.clear()
                ans.append(c)
        ans.extend(stack)
        return ''.join(ans)


s = Solution()
print(s.reverseStr('abcdefghijk', 2))
print(s.reverseStr('', 2))
print(s.reverseStr('ab', 3))
print(s.reverseStr('abcd', 3))

