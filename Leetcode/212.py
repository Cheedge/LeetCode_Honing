"""
212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.



Example 1:


Input:
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.child = dict()
        self.end = False

    def add(self, w: str) -> None:
        """
        Store all the charactors of every word.
        Loop every char of w, if it not in the Trie,
        make a new node and add char into it.
        """
        cur = self
        for char in w:
            if char not in cur.child:
                cur.child[char] = TrieNode()
            cur = cur.child[char]
        cur.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        seen = set()
        remain_words = len(words)
        self.res: List[str] = list()
        # Store all the charactors of every word as a Trie.
        for w in words:
            root.add(w)

        # dfs
        def DFS(r, c, node, path):
            if (
                r < 0
                or r >= m
                or c < 0
                or c >= n
                or board[r][c] not in node.child
                or remain_words <= 0
                or (r, c) in seen
            ):
                return

            seen.add((r, c))
            path += board[r][c]
            node = node.child[board[r][c]]
            # check word exist in words
            if node.end:
                self.res.append(path)
                node.end = False

            DFS(r - 1, c, node, path)
            DFS(r + 1, c, node, path)
            DFS(r, c + 1, node, path)
            DFS(r, c - 1, node, path)
            seen.remove((r, c))

        # main
        for i in range(m):
            for j in range(n):
                DFS(i, j, root, "")
        return self.res
