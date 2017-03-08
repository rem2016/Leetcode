# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/27/ 20:34


73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
https://leetcode.com/problems/set-matrix-zeroes/?tab=Description
"""

__author__ = "Rem"

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [0 for _ in range(m)], [0 for _ in range(n)]
        for i, r in enumerate(matrix):
            for j, v in enumerate(r):
                if v == 0:
                    row[i] = 1
                    col[j] = 1

        for i, r in enumerate(matrix):
            for j, v in enumerate(r):
                if row[i] or col[j]:
                    matrix[i][j] = 0

def test(v):
    s = Solution()
    a = v
    s.setZeroes(a)
    print(a)
    print('=' * 20)

test([[0,1,2,3]])
test([[0,1,2,3],[1,2,3,4]])
