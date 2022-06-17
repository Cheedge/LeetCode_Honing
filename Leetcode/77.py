"""
77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""
def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    # (4, 2) -> 4 + (3, 2) -> 3 + (2, 2)
    res = list()
    # if n == 1 and k == 1: return [[1]]
    # if n == 1 and k > 1: return
    for n1 in range(n, k-1, -1):
        if k>1:
            # eg. (4,3)-> [4,3,2], [4,3,1], [4,2,1] + [3,2,1]
            # eg. (3,1)-> [3,2], [3,1], + [2,1]
            for it in combine(n1-1, k-1):
                # C[k-1, n-1]
                tmp = [n1]
                tmp.extend(it)
                res.append(tmp)
        if k==1: return [[i] for i in range(1, n1+1)]
    return res