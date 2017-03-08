# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/20/ 19:49 
"""

__author__ = "Rem"
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[%d, %d]' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        assert isinstance(intervals, list)
        intervals.sort(key=lambda x: x.start*2147483648 + x.end)
        print(intervals)
        ans = []
        i = 0
        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            for i in range(i, len(intervals)+1):
                if i == len(intervals):
                    break
                if end > intervals[i].end:
                    continue
                if end < intervals[i].start:
                    break
                end = intervals[i].end
            ans.append(Interval(start, end))
        print(ans)
        return ans




s = Solution()
s.merge([Interval(1,2), Interval(5,9), Interval(3, 10), Interval(5, 11)])
s.merge([Interval(1,3), Interval(2,6), Interval(8, 10), Interval(15,18)])
