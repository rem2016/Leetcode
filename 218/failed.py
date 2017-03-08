# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/28/ 15:24

https://leetcode.com/problems/the-skyline-problem/?tab=Description
"""

__author__ = "Rem"


class TreeNode:
    def __init__(self, v):
        self.max_v = v
        self.l_bound = None
        self.r_bound = None

    def __repr__(self):
        t = self.max_v
        if t is None:
            t = 'n'
        return '(' + str(t) + ' ' + str(self.l_bound) + ' ' + str(self.r_bound) + ')'


class SegmentTree:
    def __init__(self, max_length):
        self.nodes = [TreeNode(0) for _ in range(max_length * 4)]
        self._build(1, 0, max_length - 1)
        self.set(0, 0, max_length - 1)

    def _build(self, index, l, r):
        self.nodes[index].l_bound = l
        self.nodes[index].r_bound = r
        if l == r: return
        self._build(index * 2, l, (l + r) // 2)
        self._build(index * 2 + 1, (l + r) // 2 + 1, r)

    def _set(self, index, v, l, r):
        if index >= len(self.nodes):
            print(index, v, l, r)
            raise AssertionError("On SegmentTree._set, index >= len(self.nodes)")
        if v is None:
            return
        node = self.nodes[index]
        if node.l_bound is None:
            return
        if node.l_bound == l and node.r_bound == r:
            if node.max_v is None or v > node.max_v:
                node.max_v = v
            return
        m = (node.l_bound + node.r_bound) // 2
        if l <= m:
            self._set(index * 2, v, l, min(m, r))
        if r > m:
            self._set(index * 2 + 1, v, max(m + 1, l), r)

    def set(self, v, l, r):
        self._set(1, v, l, r)

    def _put_down(self, node_index):
        node = self.nodes[node_index]
        l, r = node.l_bound, node.r_bound
        if l == r:
            return
        m = (l + r) // 2
        self._set(node_index * 2, node.max_v, l, m)
        self._set(node_index * 2 + 1, node.max_v, m + 1, r)
        node.max_v = None

    def get_max_list(self):
        ans = []
        for i in range(0, len(self.nodes)):
            if self.nodes[i].l_bound is None:
                continue
            if self.nodes[i].l_bound == self.nodes[i].r_bound:
                ans.append(self.nodes[i])
            else:
                self._put_down(i)
        ans.sort(key=lambda x: x.l_bound)
        return ans


class Solution(object):
    def __init__(self):
        self.code = None

    def zip_encode(self, buildings):
        a_list = []
        the_map = {}
        n_map = {}
        for i, v in enumerate(buildings):
            for t in [0, 1]:
                if v[t] not in the_map:
                    the_map[v[t]] = None
                    a_list.append((v[t], i*2+t))
        the_map.clear()
        a_list.sort(key=lambda x: x[0])
        for i, c in enumerate(a_list):
            height, index = c
            t = buildings[index // 2][index % 2]
            if t not in the_map:
                the_map[t] = i
                n_map[i] = t
            buildings[index // 2][index % 2] = the_map[t]
        print(buildings)
        self.map = the_map
        self.nmap = n_map
        return len(self.map.keys())

    def zip_decode(self, pos):
        if pos not in self.nmap:
            return None
        return self.nmap[pos]

    def _print_nodes(self, nodes):
        last_2 = 2
        for i in range(1, len(nodes)):
            print(nodes[i], end='\t')
            if (i + 1) % last_2 == 0:
                last_2 *= 2
                print('')
        print('\n@@@@')

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        i = 1
        while i < len(buildings):
            if buildings[i][0] > buildings[i - 1][1]:
                buildings.insert(i, [buildings[i - 1][1], buildings[i][0], 0])
                i += 1
            elif buildings[i-1][1] > buildings[i][0]:
                buildings.insert(i, [buildings[i][0], buildings[i-1][1], buildings[i-1][2]])
                buildings[i-1][1] = buildings[i][0]
                i += 1
            elif buildings[i][0] == buildings[i-1][0] and buildings[i][1] == buildings[i-1][1]:
                buildings[i-1][2] = max(buildings[i-1][2], buildings[i][2])
                del buildings[i]
                i -= 1
            i += 1
        max_length = self.zip_encode(buildings)
        tree = SegmentTree(max_length*2)
        for building in buildings:
            tree.set(building[2], building[0], building[1])
        self._print_nodes(tree.nodes)
        _ans = tree.get_max_list()
        self._print_nodes(tree.nodes)
        # print('=======')
        _ans = [(v.max_v, self.zip_decode(v.l_bound)) for v in _ans if self.zip_decode(v.l_bound) is not None]
        print('_ans', _ans)
        print('code', self.code)
        ans = []
        i = 0
        pre_r = _ans[i][1]
        while i < len(_ans):
            v, l = _ans[i]
            while i + 1 < len(_ans) and _ans[i + 1][0] == v:
                i += 1
            r = _ans[i][1]
            _for_r = 1
            while pre_r == r:
                r = self.zip_decode(self.map[r] + _for_r)
                _for_r += 1
            ans.append([pre_r, v])
            pre_r = r
            i += 1
        if ans[-1][1] != 0:
            ans.append([pre_r, 0])
        return ans


def test(*args):
    s = Solution()
    print(s.getSkyline(*args))


# test([[1,100,100],[1,100,50],[1,100,3],[50,200,10], [50,200,3],[5, 201, 6]])
# test([[1, 5, 1], [1, 4, 2], [1, 2, 3]])
# test([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]])
# test([[2, 4, 7], [2, 5, 5], [2, 6, 6]])
# test([[1, 3, 100]])
# test([[1, 3, 100], [2, 9, 10]])
# test([[0, 1, 3], [1, 2, 3]])
test([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]])
# test([[2, 5, 7], [3, 5, 5], [4, 5, 6]])
# test([[0, 2, 100], [1, 3, 30]])
# test([[0, 2, 100]])
# test([])
# test([[1, 2, 1], [1, 2, 2], [1, 2, 3]])
