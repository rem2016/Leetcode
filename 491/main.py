# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/08/ 17:26 
"""

__author__ = "Rem"


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return []
        groovy = [nums[0]]
        ans = [[nums[0]]]
        last_index = [1]
        for i in range(1, len(nums)):
            print(groovy)
            for j in range(len(groovy) - 1, -2, -1):
                if j < 0 or groovy[j] <= nums[i]:
                    break
            groovy = groovy[:j + 1]
            groovy.append(nums[i])

            last_value_list = [groovy[-1]]
            if j >= 0:
                for index in range(last_index[j]):
                    ans.append(ans[index] + last_value_list)
            ans.append(last_value_list)
            last_index.append(len(ans))
        for i in range(len(last_index) - 1, -1, -1):
            del ans[last_index[i] - 1]
        print(groovy)
        return ans


def test(*args):
    s = Solution()
    print(s.findSubsequences(*args))


if __name__ == '__main__':
    # test([i for i in range(15)])
    # test([1,2,3,4,5])
    test([3,2,1])
    test([3,2,1,5])
