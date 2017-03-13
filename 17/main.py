# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/13/ 20:33 
"""

__author__ = "Rem"


class Solution(object):
    def __init__(self):
        self.code = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.digits = None
        self.ans = None

    def _conbinations(self, index, current_ans=None):
        if current_ans is None:
            current_ans = [''] * 100
        code = self.code[self.digits[index]]
        for c in code:
            if c != '*':
                current_ans[index] = c
            if len(self.digits) == index + 1:
                s = ''.join(current_ans)
                if s:
                    self.ans.append(s)
            else:
                self._conbinations(index + 1, current_ans)


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        self.ans = []
        self.digits = [int(x) for x in digits]
        self._conbinations(0, )
        return self.ans


s = Solution()
print(s.letterCombinations('11213'))
print(s.letterCombinations(''))
print(s.letterCombinations('0'))
print(s.letterCombinations('1111020'))


