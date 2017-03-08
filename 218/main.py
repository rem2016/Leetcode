# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/28/ 20:38 
"""

__author__ = "Rem"


from queue import PriorityQueue
from functools import cmp_to_key
from heapq import _siftdown


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        scan = []
        for b in buildings:
            scan.append([b[0], -b[2]])
            scan.append([b[1],  b[2]])
        scan.sort(key=cmp_to_key(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1]))
        q = PriorityQueue()
        q.put(0)
        ans = []
        prev = None
        for h in scan:
            if h[1] < 0:
                q.put(h[1])
            else:
                index = q.queue.index(-h[1])
                q.queue[index] = -2147483647
                _siftdown(q.queue, 0, index)
                q.get()
            top = -q.queue[0]
            if top != prev:
                ans.append([h[0], top])
                prev = top
        return ans

def test(*args):
    s = Solution()
    print(s.getSkyline(*args))


# test([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
test([[3,7,8],[3,8,7],[3,9,6],[3,10,5],[3,11,4],[3,12,3],[3,13,2],[3,14,1]])

