"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        # res = False
        for i in range(m):
            for j in range(n):
                visited = set()
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    # DFS
                    if self.DFS(board, i, j, word[1:], visited):
                        return True
        return False
                    
                    
                    
                    
    def DFS(self, board, i, j, word, visited):
        visited.add((i, j))
        m, n = len(board), len(board[0])
        # print(i, j, word, visited)
        # if board[i][j] == word[0]:
        if len(word)==0:
            return True
        res = False
        if i>0 and board[i-1][j] == word[0] and (i-1, j) not in visited:
            if self.DFS(board, i-1, j, word[1:], visited):
                res = True
            else:
                visited.remove((i-1, j))
        if i<m-1 and board[i+1][j] == word[0] and (i+1, j) not in visited:
            if self.DFS(board, i+1, j, word[1:], visited):
                res = True
            else:
                visited.remove((i+1, j))
        if j>0 and board[i][j-1] == word[0] and (i, j-1) not in visited:
            if self.DFS(board, i, j-1, word[1:], visited):
                res = True
            else:
                visited.remove((i, j-1))
        if j<n-1 and board[i][j+1] == word[0] and (i, j+1) not in visited:
            if self.DFS(board, i, j+1, word[1:], visited):
                res = True
            else:
                visited.remove((i, j+1))
        return res