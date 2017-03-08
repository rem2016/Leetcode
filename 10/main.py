# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/21/ 16:33 
"""

__author__ = "Rem"


def reformat(s):
    repeat = ''
    i = 0
    new_s = []
    while i < len(s):
        if s[i] == '*':
            repeat = s[i - 1]
            i += 1
            while i < len(s) and repeat == s[i]:
                if i+1 < len(s) and s[i+1] == '*':
                    i += 2
                    continue
                new_s.append(repeat)
                i += 1
            new_s[-1] += '*'
            repeat = ''
            continue
        if not repeat:
            new_s.append(s[i])
            i += 1
            continue
    return new_s


def toMatch(s, p):
    print(p)
    if not p:
        if not s:
            return True
        return False
    pi, si = 0, 0
    if not s:
        while pi < len(p) and p[pi][-1] == '*':
            pi += 1
        return pi == len(p)
    match = True
    while si < len(s) and pi < len(p):
        if s[si] == p[pi] or p[pi] == '.':
            si += 1
            pi += 1
            continue
        if p[pi][-1] != '*':
            match = False
            break
        # case that exits '*'
        match = False
        while si < len(s) and (p[pi][0] == '.' or s[si] == p[pi][0]):
            match = toMatch(s[si:], p[pi+1:])
            if not match:
                si += 1
                continue
            else: break
        if not match and si == len(s):
            while pi < len(p) and p[pi][-1] == '*':
                pi += 1
            if si == len(s) and pi == len(p):
                match = True
        elif not match:
            return toMatch(s[si:], p[pi+1:])
        return match
    if si != len(s):
        match = False
    while pi < len(p) and p[pi][-1] == '*':
        pi += 1
    if pi != len(p):
        match = False
    return match


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = reformat(p)
        return toMatch(s, p)
# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/21/ 16:33
"""

__author__ = "Rem"


def reformat(s):
    repeat = ''
    i = 0
    new_s = []
    while i < len(s):
        if s[i] == '*':
            repeat = s[i - 1]
            i += 1
            while i < len(s) and repeat == s[i]:
                if i+1 < len(s) and s[i+1] == '*':
                    i += 2
                    continue
                new_s.append(repeat)
                i += 1
            new_s[-1] += '*'
            repeat = ''
            continue
        if not repeat:
            new_s.append(s[i])
            i += 1
            continue
    return new_s


def toMatch(s, p):
    print(p)
    if not p:
        if not s:
            return True
        return False
    pi, si = 0, 0
    if not s:
        while pi < len(p) and p[pi][-1] == '*':
            pi += 1
        return pi == len(p)
    match = True
    while si < len(s) and pi < len(p):
        if s[si] == p[pi] or p[pi] == '.':
            si += 1
            pi += 1
            continue
        if p[pi][-1] != '*':
            match = False
            break
        # case that exits '*'
        match = False
        while si < len(s) and (p[pi][0] == '.' or s[si] == p[pi][0]):
            match = toMatch(s[si:], p[pi+1:])
            if not match:
                si += 1
                continue
            else: break
        if not match and si == len(s):
            while pi < len(p) and p[pi][-1] == '*':
                pi += 1
            if si == len(s) and pi == len(p):
                match = True
        elif not match:
            return toMatch(s[si:], p[pi+1:])
        return match
    if si != len(s):
        match = False
    while pi < len(p) and p[pi][-1] == '*':
        pi += 1
    if pi != len(p):
        match = False
    return match


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = reformat(p)
        return toMatch(s, p)



def test(ans, *args):
    s = Solution()
    if s.isMatch(*args) != ans:
        print('Error case:', args)



if __name__ == '__main__':
    # test(True, '123','.*')
    # test(True, '','.*')
    # test(True, '','2*')
    # test(False, '1234','.*345')
    # test(True, '1234','.*34')
    # test(True, '1234','1.*3.*.*.*4')
    # test(True, '1234','1.*3*.*.*34')
    # test(False, '1111312312','1*.*.*.*3.*3.*22')
    test(True, 'aaa', 'ab*a*c*a*')

