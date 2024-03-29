"""
188. Best Time to Buy and Sell Stock IV
Hard
(121, 122, 123)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54125/Very-understandable-solution-by-reusing-Problem-III-idea

You are given an integer array prices where prices[i] is the price of a given stock
on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must
sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # buy[i] = max(last profit - pay = sell[i-1] - prices[i])
        # sell[i] = max(last cost + pay = buy[i] + prices[i])
        # buy[0], sell[0] = 0, len(buy)=len(sell)=k+1
        # loop over all prices
        buy, sell = [int(-float("inf"))] * (k + 1), [0] * (k + 1)
        n = len(prices)
        # special case: k>n/2, can sum up all prices[i]<prices[i+1]
        if k > (n / 2):
            res = 0
            for i in range(1, n):
                if prices[i - 1] < prices[i]:
                    res += prices[i] - prices[i - 1]
            return res
        for j in range(n):
            for i in range(1, k + 1):
                buy[i] = max(buy[i], sell[i - 1] - prices[j])
                sell[i] = max(sell[i], buy[i] + prices[j])
        # print(buy, sell)
        return sell[k]
