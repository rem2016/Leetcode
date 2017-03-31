# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/27/ 21:11 
"""

__author__ = "Rem"


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # if len(nums) < 15:
        #     return min(nums)
        l, r = 0, len(nums)
        while l < r-1 and nums[l] >= nums[r-1]:
            print(l, r-1, nums[l], nums[r-1])
            m = (l + r) // 2
            if nums[l] == nums[r-1]:
                if nums[m] == nums[l]:
                    l += 1
                    r -= 1
                    continue
            if nums[l] < nums[m]:
                l = m
            elif nums[r-1] >= nums[m]:
                r = m + 1
            else:
                l = m
        return nums[l]

s = Solution()
print(s.findMin([3,4,5,6,7,8,9,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]))
print('\n\n\n')
print(s.findMin([266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38]))
print(s.findMin([3,4,5,1,2]))
print(s.findMin([3,4,5,100,200,0.5,1,2,]))
print(s.findMin([1,2,4,5,6]))
print(s.findMin([1,2,4,5,6,0]))


