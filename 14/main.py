# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/11/ 11:36 
"""

__author__ = "Rem"


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ""
        s = strs[0]
        end = len(s)
        j = end
        for i in range(1, len(strs)):
            for j in range(end):
                if j >= len(strs[i]) or s[j] != strs[i][j]:
                    break
                j += 1
            end = j
        return s[:end]


s = Solution()
print(s.longestCommonPrefix(['123','123','12341231231321312','12312']))
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(['1234']))
print(s.longestCommonPrefix(['', '', '','']))

