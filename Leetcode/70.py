"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""
class Solution(object):
    def __init__(self):
        self.repo = {1: 1, 2: 2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # recursion
        # every step self.climbStairs(n-1) + self.climbStairs(n-2)
        # last step: climbStairs(2) = 2, climbStairs(1)=1
        # 4 ->  3 + 1 or 2 + 2
        #       3 ->2 + 1
        #           2 -> 1 + 1 or 2
        
        res = 0
        # repo = {1: 1, 2: 2} 注意这种方法在递归中用字典，每次会新造一个所以没用处
        if n-2>0:
            if n in self.repo:
                res = self.repo[n]
            else:
                res = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.repo.update({n: res})        
        elif n == 2:
            res = 2
        else:
            res = 1
        return res
"""

# Top down - TLE
def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1)+self.climbStairs(n-2)
 
# Bottom up, O(n) space
def climbStairs2(self, n):
    if n == 1:
        return 1
    res = [0 for i in range(n)]
    res[0], res[1] = 1, 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]
    return res[-1]

# Bottom up, constant space
def climbStairs3(self, n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in range(2, n):
        tmp = b
        b = a+b
        a = tmp
    return b
    
# Top down + memorization (list)
def climbStairs4(self, n):
    if n == 1:
        return 1
    dic = [-1 for i in range(n)]
    dic[0], dic[1] = 1, 2
    return self.helper(n-1, dic)
    
def helper(self, n, dic):
    if dic[n] < 0:
        dic[n] = self.helper(n-1, dic)+self.helper(n-2, dic)
    return dic[n]
    
# Top down + memorization (dictionary)  
def __init__(self):
    self.dic = {1:1, 2:2}
    
def climbStairs(self, n):
    if n not in self.dic:
        self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    return self.dic[n]

class Solution:
    def climbStairs(self, n, d = {1:1, 2:2}):
        if n == 0: return 0
        
        if n not in d:
            d[n] = self.climbStairs(n-1, d) + self.climbStairs(n-2, d)
        return d[n]
!!!!!!!!!!!!!!!!!!!!!!!这样的recursion才可以，因为将dict传递给每次调用!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""