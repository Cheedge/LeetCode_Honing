"""
509. Fibonacci Number
"""
class Solution(object):
    def __init__(self):
        self.memo = {0: 0, 1: 1}
    
    def fib(self, n):
        # recursion + memory = DP
        # memo = {0: 0, 1: 1}
        if n<2: return n
        # ans = 0
        if n>=2 and n not in self.memo:
            self.memo[n] = self.fib(n-1)+self.fib(n-2)
            # self.memo[n] = ans
            # print(self.memo)
            
        return self.memo[n]