"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
Medium

You are given a rectangular cake of size h*w and two arrays of integers horizontalCuts and verticalCuts
where:

horizontalCuts[i] is the distance from the top of the rectangular cake
to the ith horizontal cut and similarly, and verticalCuts[j] is 
the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut 
at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts.
Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake.
Red lines are the horizontal and vertical cuts. After you cut the cake,
the green piece of cake has the maximum area.
Example 2:

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake.
Red lines are the horizontal and vertical cuts. After you cut the cake,
the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 109
1 <= horizontalCuts.length <= min(h - 1, 105)
1 <= verticalCuts.length <= min(w - 1, 105)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
All the elements in horizontalCuts are distinct.
All the elements in verticalCuts are distinct.
"""
def maxArea(h, w, horizontalCuts, verticalCuts):
    """
    :type h: int
    :type w: int
    :type horizontalCuts: List[int]
    :type verticalCuts: List[int]
    :rtype: int
    """
    # append h,w to horiazontal, vertical O(1) and sort O(nlogn)
    # cal diff of horizantal and vertical and find max O(n) O(n)
    # cal A= width * height
    horizontalCuts.append(h)
    horizontalCuts.sort()
    verticalCuts.append(w)
    verticalCuts.sort()
    width, height = horizontalCuts[0], verticalCuts[0]
    for i in range(1, len(horizontalCuts)):
        width = max(width, horizontalCuts[i]-horizontalCuts[i-1])
    for i in range(1, len(verticalCuts)):
        height = max(height, verticalCuts[i]-verticalCuts[i-1])
    return width * height % (10**9 + 7)