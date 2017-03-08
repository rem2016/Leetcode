# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/20/ 21:02 
"""

__author__ = "Rem"


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        pri = {'+': 0, '-': 0, '*': 1, '/': 1}
        op_stack = []
        stack = []
        i = 0

        def iter_i():
            t = i + 1
            while t!=len(s) and s[t] == ' ':
                t += 1
            return t
        while i < len(s):
            num = 0
            while i!=len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i = iter_i()
            stack.append(num)
            if i == len(s):
                break

            while op_stack and pri[op_stack[-1]] >= pri[s[i]]:
                stack.append(op_stack.pop())
            op_stack.append(s[i])

            i = iter_i()

        while op_stack:
            stack.append(op_stack.pop())
        num_stack = []
        print(stack)
        stack.reverse()
        op_func = {'+':lambda a,b: a+b,
                   '-':lambda a,b: a-b,
                   '*':lambda a,b: a*b,
                   '/':lambda a,b: a//b,}
        while stack:
            top = stack.pop()
            if isinstance(top, int):
                num_stack.append(top)
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                num_stack.append(op_func[top](a,b))
        return num_stack[0]

s = Solution()
print(s.calculate('1 + 3 / 3 + 5 / 5 + 10 / 2 - 8'))
print(s.calculate('1 - 1'))
print(s.calculate('4*3 - 12 + 5 - 5'))
print(s.calculate('8 * 7 + 56 / 8 - 7 - 56'))
print(s.calculate('    5 + 5 *    5 / 5 / 5 -       6'))
print(s.calculate('4 + 3*3 - 13'))
print(s.calculate('4*3 - 12 + 5 - 5'))








