"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path, res = "", list()
        self.DFS(n, n, path, res)
        return res
        
        
        
        
        
    def DFS(self, left, right, path, res):
        # print(path, left, right)
        if left==0 and right==0:
            res.append(path)
            return
        if left>0:
            self.DFS(left-1, right, path+"(", res)
        if right>left and right>0:
            self.DFS(left, right-1, path+")", res)