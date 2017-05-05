# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/04/07/ 21:19 
"""

__author__ = "Rem"




class Solution(object):
    def _isNum(self, s):
        if len(s) == 0:
            return False
        if len(s) == 1:
            if not s.isdigit():
                return False
        dot_num = 0
        has_e = 0
        is_neg = False
        is_begin = True
        has_digit = False
        for i in range(len(s)):
            if s[i] == '-' or s[i] == '+':
                if is_neg or not is_begin:
                    return False
                is_neg = True
                continue
            elif s[i] == '.':
                dot_num += 1
                if i + 1 < len(s) and not s[i + 1].isdigit():
                    return False
                continue
            elif s[i] == 'e':
                if is_begin or has_e:
                    # begin with e
                    return False
                has_e = i + 1
                break
            elif not s[i].isdigit():
                return False
            else:
                has_digit = True
            is_begin = False
        if dot_num > 1:
            return False
        if has_e and has_digit:
            if has_e >= len(s):
                # end with e
                return False
            for i in range(has_e, len(s)):
                if not s[i].isdigit():
                    # is not digit
                    return False
        return has_digit

    def _isInt(self, s):
        if len(s) <= 0:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if len(s) <= 0:
            return False
        return s.isdigit()

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        s = s.split('e')
        if len(s) == 1:
            return self._isNum(s[0])
        if len(s) == 2:
            return self._isNum(s[0]) and self._isInt(s[1])
        return False


s = Solution()
test = ('-123e123', '-.e', 'e12.3', '43.e3.', '43.e3', '23e+123', '123e-12', '0e')
for i in test:
    print(s.isNumber(i))

