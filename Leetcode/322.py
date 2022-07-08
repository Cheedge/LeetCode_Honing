"""
322. Coin Change
Medium

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    # dp[i]: when coin target is i, how many ways to get
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1
    
    # @lru_cache
    # def recursion(i):
    #     if i==0: return 0
    #     if i<0: return float('inf')
    #     return min(recursion(i-coin)+1 for coin in coins)
    # return recursion(amount) if recursion(amount)!=float('inf') else -1