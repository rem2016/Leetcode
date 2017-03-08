# -*- coding: utf-8 -*-
"""

@author: Rem
@contack: remch183@outlook.com
@time: 2017/02/20/ 15:32 
"""

__author__ = "Rem"


def buildTree(startWord, endWord, wordList):
    """
    use bfs to build parents tree. first step there is only one

    Here we need to prevent parent loop. Because the character
    of the search method, the loop length can only be two, so in bfs
    we can only save the previous layer and current layer.
    :return: parent tree
    """
    # dict<string, set(parents)>
    parent = {}

    def append(word, parent_word):
        parent.setdefault(word, set())
        parent[word].add(parent_word)

    current_layer = set([startWord])
    next_layer = set()
    pre_layer = set()
    foundEnd = False
    while not foundEnd and len(current_layer):
        next_layer.clear()
        for word in current_layer:
            for index in range(len(word)):
                for alpha in range(ord('a'), ord('z') + 1):
                    if chr(alpha) == word[index]:
                        continue
                    new_word = word[:index] + chr(alpha) + word[index + 1:]
                    if new_word not in wordList:
                        continue
                    if new_word == endWord:
                        append(word, new_word)
                        foundEnd = True
                        continue
                    if new_word in pre_layer or new_word in current_layer:
                        continue
                    append(word, new_word)
                    if new_word in current_layer or new_word in next_layer:
                        continue
                    next_layer.add(new_word)
        next_layer, current_layer, pre_layer = pre_layer, next_layer, current_layer
    return parent


def findPath(start, end, path, paths, parents):
    # found one answer
    if start == end:
        paths.append(list(path))
        return
    if start not in parents:
        return
    for nextword in parents[start]:
        path.append(nextword)
        findPath(nextword, end, path, paths, parents)
        path.pop()


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        parents = buildTree(beginWord, endWord, wordList)
        ladders = []
        path = [beginWord]
        findPath(beginWord, endWord, path, ladders, parents)
        return ladders



s = Solution()
# print(s.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(s.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", ]))

print(s.findLadders('aaa', 'bbb', ["aab", "aba", "bab", "baa", "bba", "bbb","abb"]))
print(s.findLadders('red', 'tax', ["ted","tex","red","tax","tad","den","rex","pee"]))
