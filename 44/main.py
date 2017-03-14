# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 19:25 
"""

__author__ = "Rem"


class Solution(object):
    def find_all(self, pattern, s, begin):
        i = begin
        ans = []
        while i < len(s) - len(pattern)+1:
            fail = False
            for k in range(i, i + len(pattern)):
                if pattern[k - i] == '?':
                    continue
                if pattern[k - i] != s[k]:
                    fail = True
                    break
            if not fail:
                ans.append(i)
            i += 1
        return ans

    def isMatch(self, s, p, i=0, j=0):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            if len(s) == 0:
                return True
            return False
        ss = []
        i = 0
        while i < len(p):
            if p[i] == '*':
                if i == 0 or p[i - 1] != '*':
                    ss.append(p[i])
            else:
                begin = i
                for end in range(i, len(p)):
                    if p[end] == '*':
                        break
                if p[end] != '*':
                    end += 1
                ss.append(p[begin:end])
                i = end - 1
            i += 1
        index = []
        pre_min_index = 0
        for i in range(len(ss)):
            if ss[i] == '*':
                index.append((0,))
                continue
            index.append(self.find_all(ss[i], s, pre_min_index))
            if not index[-1]:
                return False
            pre_min_index = index[-1][0] + len(ss[i])
            if i == len(ss) - 1:
                index[-1] = [index[-1][-1]]
                if index[-1][0] != len(s) - len(ss[i]):
                    return False
            if i == 0:
                index[-1] = [index[-1][0]]
                if index[-1][0] != 0:
                    return False
        pre_index = 0
        for string, lst in zip(ss, index):
            if string == '*':
                continue
            found = False
            for k in lst:
                if k >= pre_index:
                    pre_index = k + len(string)
                    found = True
                    break
            if not found:
                return False
        return True

s = Solution()
print(s.isMatch('aaaaaa', 'aa'))
print(s.isMatch('123', '1*?3'))
print(s.isMatch('123', '1*23'))
print(s.isMatch('123123123', '1*3****'))
print(s.isMatch('123', '123'))
print(s.isMatch('1234', '123'))
print(s.isMatch('1234', '1235'))
print(s.isMatch('123', ''))
print(s.isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
                "*a*a*a*a*a*a*a*a*a*a*a*abzvasdf*a*a*a*a*a*a*a*a*a*a*a"))
print(s.isMatch('123', '1**2*3'))
