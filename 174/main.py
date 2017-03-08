# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/28/ 14:47 
"""

__author__ = "Rem"


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n, m = len(dungeon), len(dungeon[0])
        direction = ((0, -1), (-1, 0))
        min_health = [[0 for i in range(m)] for _ in range(n)]
        que = [(n-1, m-1)]
        while que:
            x, y = que.pop()
            if x - 1 >= 0 and min_health[x-1][y] == 0:
                que.insert(0, (x-1, y))
                min_health[x-1][y] = -1
            if y - 1 >= 0 and min_health[x][y-1] == 0:
                que.insert(0, (x, y-1))
                min_health[x][y-1] = -1
            if x == n-1 and y == m-1:
                min_health[x][y] = max(1, 1-dungeon[x][y])
                continue
            right_health = 2147483647
            bottom_health = 2147483647
            if y + 1 < m:
                right_health = min_health[x][y+1]
            if x + 1 < n:
                bottom_health = min_health[x + 1][y]
            min_health[x][y] = max(
                min(right_health, bottom_health) - dungeon[x][y],
                1,
                1 - dungeon[x][y])

        print('=' * 20)
        for t in min_health:
            print(t)
        return min_health[0][0]


def test(*args):
    s = Solution()
    print(s.calculateMinimumHP(*args))


if __name__ == "__main__":
    test([[-1, 0, 0],
          [0, 5, 0],
          [0, 0, -9]])

    test([[-1, 0, 0],
          [-10, 5, 0],
          [20, 100, -9]])

