"""
218. The Skyline Problem
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city
when viewed from a distance. Given the locations and heights of all the buildings,
return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings
where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate
in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment
in the skyline except the last point in the list, which always has a y-coordinate 0
and is used to mark the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
the three lines of height 5 should be merged into one in the final output
as such: [...,[2 3],[4 5],[12 7],...]


Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent
the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]


Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""
from collections import defaultdict
from heapq import heappop, heappush

import sortedcontainers


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heapify, heappop, heappush

        # scan[x][h][s]: x-coordinate, -height, string(enter, leave)
        # use -height because heapq is min heap
        scan = list()
        for x1, x2, height in buildings:
            scan.append((x1, -height, "enter"))
            scan.append((x2, -height, "leave"))
        scan.sort()
        # if height change, then record
        #   1. height increase: add the x, record heighest height
        #   2. height decrease: remvoe x, record heighest height
        # use heap to store data(keep the heighest at top)
        heap = list()
        prevMaxH = 0
        # use the list to store answer
        ans = list()
        repo = dict()
        for x, h, s in scan:
            if s == "enter":
                heappush(heap, h)
            else:
                if h > prevMaxH:
                    heap.remove(h)
                    # keep heap
                    heapify(heap)
                else:  # when h == prevMaxH
                    if heap:
                        heappop(heap)
            # if height change then add to ans
            if heap:
                curMaxH = heap[0]
            else:
                curMaxH = 0
            if curMaxH != prevMaxH:
                if x in repo:
                    ans.pop(repo[x])
                    # ans.append([x, -curMaxH])
                else:
                    repo[x] = len(ans)
                    # ans.append([x, -curMaxH])
                ans.append([x, -curMaxH])
                prevMaxH = curMaxH
        return ans

    # https://leetcode.com/problems/the-skyline-problem/solutions/2642634/python-sorting-and-sorted-list-solution-o-nlogn-time-o-n-space/
    # import sortedcontainers
    # class Solution(object):
    def getSkyline1(self, buildings):
        points = []
        # * Build the start and the end points of the
        # * x coordinate along with their heights.
        for start, end, height in buildings:
            # * Insert the x coordinate start point with height as negative
            # * value to handle all the 3 edge cases while sorting it.
            points.append((start, -height))
            points.append((end, height))

        # * This handles all the 3 edge cases as we're storing
        # * the start point heights as negative values.
        points.sort()
        # * Using SortedList instead of Priority Queue (Max Heap) to
        # * support the removal of a given element in O(logn) time.
        heights = sortedcontainers.SortedList([0])
        # heights = [0]
        res = []

        for point in points:
            x, height = point
            # * If the height is less than 0 then it indicates the start point
            # * in which case we insert the height into the SortedList.
            if height < 0:
                heights.add(-height)
                # heappush(heights, -height)
            # * Else it indicates the end point in which case
            # * we remove the height from the SortedList.
            else:
                heights.remove(height)
                # heappop(heights)

            # * Add the point to the result iff the max height has been changed.
            if not res or res[-1][1] != heights[-1]:
                res.append([x, heights[-1]])

        return res

    # https://leetcode.com/problems/the-skyline-problem/solutions/2643582/python-easy-to-understand-sweep-line-approach-o-n-log-n-time-detailed-explanation/

    # class Solution:
    def getSkyline2(self, buildings):
        events, sweepline, ans = [], [], []
        # We count the occurences of a specific height. Thus, we are able
        # to handle duplicate heights.
        heights = defaultdict(int)
        for start, end, height in buildings:
            # We sweep from left to right. If an insertion into the sweepline
            # happens at the same x-coordinate as the deletion of an element from
            # the sweepline, then the insertion operation is handled first.
            heappush(events, [start, False, height])
            heappush(events, [end, True, height])
        while events:
            x, delete, height = heappop(events)
            if not delete:
                if not sweepline or height > -sweepline[0]:
                    # if sweepline and height > -sweepline[0]:
                    # Filter out collinear points, i.e., points that share a
                    # common x-coordinate along our skyline.
                    if ans and ans[-1][0] == x:
                        ans = ans[:-1]
                    ans.append([x, height])
                heights[height] += 1
                heappush(sweepline, -height)
            else:
                heights[height] -= 1
                if heights[height] == 0 and height == -sweepline[0]:
                    heappop(sweepline)
                    while sweepline and heights[-sweepline[0]] == 0:
                        heappop(sweepline)
                    ans.append([x, -sweepline[0] if sweepline else 0])
        return ans
