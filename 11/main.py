# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/26/ 16:19 
"""

__author__ = "Rem"


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_ans = 0
        while l < r:
            ans = min(height[l], height[r]) * (r - l)
            if ans > max_ans:
                max_ans = ans
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_ans
