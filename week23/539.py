# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/03/12/ 11:35 
"""

__author__ = "Rem"


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def to_minite(time):
            l, r = time.split(':')
            return int(l) * 60 + int(r)

        times = list(map(to_minite, timePoints))
        times.sort()
        ans = -times[-1] + times[0] + 24*60
        for i in range(1, len(times)):
            if times[i] - times[i-1] < ans:
                ans = times[i] - times[i - 1]
        return ans


s = Solution()
print(s.findMinDifference(['12:00', '13:00', '00:00', '23:20', '23:59']))
