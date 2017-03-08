# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/18/ 23:42 
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        stack = [root]
        ans = []
        while len(stack):
            top = stack.pop()
            thisans = [str(top.val),'','']
            if top.left is not None:
                stack.append(top.left)
                thisans[1] = str(top.left.val)
            if top.right is not None:
                stack.append(top.right)
                thisans[2] = str(top.right.val)
            ans.append(','.join(thisans))
        return ';'.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return None
        def setNode(set_root, val, set_node):
            def isEqual(v, nest_node):
                if nest_node is None:
                    return False
                return v == nest_node.val

            if isEqual(val, set_root.left):
                set_root.left = set_node
            elif isEqual(val, set_root.right):
                set_root.right = set_node
            elif val < set_root.val:
                return setNode(set_root.left, val, set_node)
            else:
                return setNode(set_root.right, val, set_node)

        def createTree(val, left_v, right_v):
            new_root = TreeNode(int(val))
            if left_v != '':
                new_root.left = TreeNode(int(left_v))
            if right_v != '':
                new_root.right = TreeNode(int(right_v))
            return new_root

        data = [i.split(',') for i in data.split(';')]
        root = createTree(*data[0])
        for node in data[1:]:
            this_root = createTree(*node)
            setNode(root, int(node[0]), this_root)
        return root



# Your Codec object will be instantiated and called as such:
codec = Codec()
root = codec.deserialize('5,3,6;3,,;6,,8')
nroot = codec.deserialize(codec.serialize(root))
print(nroot)
print(codec.serialize(nroot))
root = TreeNode(0)
print(codec.serialize(root))
root = None
print(codec.serialize(root))
print(codec.deserialize(codec.serialize(root)))
