"""
126. Word Ladder II
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is
a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest
transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.
Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].


Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from collections import defaultdict, deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # TLE
        if endWord not in wordList:
            return []
        wordSet = set(wordList)
        # 1. find a word neightbour. eg: "hit"->"hot"
        #   1.1 change each letter to make a new word and check if in wordList
        # 2. BFS to find the endWord
        #   2.1 visited: set() record visited
        #   2.2 paths: list() record the path

        def find_neighbour(word):
            n = len(word)
            # neigh = list()
            for i in range(n):
                for newLetter in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + newLetter + word[i + 1 :]
                    if newWord in wordSet:
                        # neigh.append(newWord)
                        yield newWord
            # return neigh

        # BFS
        dq = deque()
        dq.append((beginWord, 0))
        # here set([]) to avoid set('hot')={'h', 'o', 't'}
        visited = set([beginWord])
        layer = dict()
        relations = defaultdict(set)
        # paths = list()
        while dq:
            w, level = dq.popleft()
            layer[w] = level
            # print("======", layer)
            # for w in ws:
            # find neighbour
            # for i in range(n):
            #     for newLetter in 'abcdefghijklmnopqrstuvwxyz':
            #         newWord = word[:i]+newLetter+word[i+1:]
            #         if newWord in wordset:
            for it in find_neighbour(w):
                relations[it].add(w)
                relations[w].add(it)
                # print(it, visited)
                if it not in visited:
                    dq.append((it, level + 1))
                    visited.add(it)
        # print(relations, layer)
        # DFS
        res, tmp = list(), list()

        def dfs(w):
            tmp.append(w)
            # print(tmp, "******", list(tmp))
            if w == endWord:
                res.append(list(tmp))
                tmp.pop()
                return
            if w in relations:
                # w has parents node in relations
                # layer: {u'cog': 4, u'hit': 0, u'log': 3, u'dog': 3, u'hot': 1, u'lot': 2, u'dot': 2}
                for p in relations[w]:
                    if layer[p] == layer[w] + 1:
                        dfs(p)
            tmp.pop()

        dfs(beginWord)
        return res
