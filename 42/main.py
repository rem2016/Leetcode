# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/26/ 17:32 
"""

__author__ = "Rem"


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        next_max = [0 for i in range(len(height))]
        now_max, max_index = 0, 0
        for i in range(len(height) - 1, 0, -1):
            if height[i] > now_max:
                now_max = height[i]
                max_index = i
            next_max[i - 1] = (now_max, max_index)

        i = 0
        ans = 0
        while i < len(height) - 1:
            # print(i, len(height))
            if height[i] > next_max[i][0]:
                ans += next_max[i][0] * (next_max[i][1] - i - 1)
                block_sum = 0
                for i in range(i + 1, next_max[i][1]):
                    block_sum += height[i]
                i += 1
                ans -= block_sum
                continue
            l = i
            block_sum = 0
            for i in range(i+1, len(height)):
                if height[l] <= height[i]:
                    break
                block_sum += height[i]
            ans += height[l] * (i - l - 1) - block_sum

        return ans

def test():
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([0]))
    print(s.trap([]))

test()


