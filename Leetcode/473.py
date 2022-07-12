"""
473. Matchsticks to Square
Medium

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick,
but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108
"""
class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        # 1. side length = perimiter*1/4 must be a int
        perim = sum(matchsticks)
        n = len(matchsticks)
        if n<4: return False
        matchsticks.sort(reverse=True)
        side_length = int(perim/4)
        if side_length * 4 != perim: return False
        
        def dfs(lefts, idx, nums):
            if idx == len(nums):
                return True
            num = nums[idx]
            used = set()
            for i, left in enumerate(lefts):
                if left >= num and left not in used:
                    lefts[i] -= num
                    if dfs(lefts, idx + 1, nums):
                        return True
                    lefts[i] += num
                    used.add(left)
            return False
        return dfs([side_length]*4, 0, matchsticks)
        

#         # 2.1 except matchstick>side_length, renturn False
#         if matchsticks[0] > side_length: return False
#         # 2.2 pop out matchstick==side_length
#         m = 0
#         while matchsticks[m]==side_length:
#             matchsticks.pop()
#             m += 1
#             if len(matchsticks)==0: return True
#         # 2.3. find 4-m(or 4-m-1) side_length from stick combinations, otherwise return False
#         # used_idx: record used matchesticks idx
#         # side_formed: how many sides remaind need to be form
#         # used_idx, side_remain = list(), 4-m-1
#         remain_idx, side_remain = {i for i in range(len(matchsticks))}, 4-m-1
#         def recurse(remain_idx, side_remain):
#             if side_remain == 0: return True
#             l, tmp = 0, []
#             print(remain_idx, side_remain)
#             idx = remain_idx.copy()
#             for i in idx:
#                 l += matchsticks[i]
#                 tmp += [i]
#                 if l==side_length:
#                     print(l, side_length, tmp)
#                     for t in tmp:
#                         remain_idx.remove(t)
#                     if recurse(remain_idx, side_remain-1):
#                         return True
#                     else:
#                         for t in tmp:
#                             remain_idx.add(t)
#                 elif l>side_length:
#                     tmp.remove(i)
#                     l -= matchsticks[i]
#             return False
        
#         return recurse(remain_idx, side_remain)
"""
[5,5,5,5,4,4,4,4,3,3,3,3]
[1,1,2,2,2]
[3,3,3,3,4]
[14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]
"""