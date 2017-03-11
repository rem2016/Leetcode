# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/11/ 11:53 
"""

__author__ = "Rem"


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            v = nums[i]
            while l < r:
                if nums[l] + nums[r] + v == 0:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] + v < 0:
                    l += 1
                else:
                    r -= 1
        return ans


s = Solution()

print(s.threeSum([-1,3, -2, 1, 0]))
print(s.threeSum([3, -2, 1, 0]))
print(s.threeSum([]))
print(s.threeSum([1]))
print(s.threeSum([1,2]))
print(s.threeSum([1,2,3]))
print(s.threeSum([1,2,-3]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,0,0,0]))
