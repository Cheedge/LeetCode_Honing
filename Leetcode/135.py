"""
135. Candy
Hard

There are n children standing in a line.
Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        find "hills": valley-peak-valley.
        assign candies from (longer) valley-peak (i++) to peak-valley(shorter) (i--).
        Binary Seach to find the peak (LC.162, LC.852, LC.2210)
        """
        # Using 2 arrays
        n = len(ratings)
        left2right, right2left = [1 for i in range(n)], [1 for i in range(n)]
        candies = 0
        # left -> right, if ratings[i] > ratings[i-1], candies[i] = candies[i-1]+1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
        # right -> left, if ratings[i] > ratings[i+1], candies[i] = candies[i+1]+1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
        for i in range(n):
            candies += max(left2right[i], right2left[i])
        return candies
