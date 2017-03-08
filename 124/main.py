# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/27/ 20:04 
"""

__author__ = "Rem"


# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)


class Solution(object):
    def __init__(self):
        self.max_ans = -2147483648

    def _maxPathSum(self, root):
        if root is None:
            return 0
        l = self._maxPathSum(root.left)
        r = self._maxPathSum(root.right)
        self.max_ans = max(self.max_ans, l + root.val, l + root.val + r, root.val + r, root.val)
        return max(root.val, root.val + l, root.val + r)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._maxPathSum(root)
        return self.max_ans


def buitTree(treelist):
    if not treelist:
        return None
    treelist.insert(0, 0)
    nodelist = [TreeNode(i) for i in treelist]
    for i in range(2, len(treelist)):
        setattr(nodelist[i // 2], ('left', 'right')[i & 1], nodelist[i])
        # print(nodelist[i])
        # print(nodelist[i//2].left, nodelist[i//2].right)
    return nodelist[1]


def test(*args):
    s = Solution()
    print(s.maxPathSum(buitTree(*args)))


if __name__ == '__main__':
    test([1, 2, 3])
