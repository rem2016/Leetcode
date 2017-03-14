# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/14/ 20:58 
"""

__author__ = "Rem"


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ans = nums[0]
        t = nums[0]
        for i in range(1, len(nums)):
            if t < 0:
                t = nums[i]
            else:
                t = nums[i] + t
            if t > max_ans:
                max_ans = t
        return max_ans

s = Solution()
print(s.maxSubArray([-1,-2,9,-3,5,6,-1]))

