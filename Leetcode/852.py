"""
852. Peak Index in a Mountain Array
Easy

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, 
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
 

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
"""
def peakIndexInMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    # return arr.index(max(arr))

    l, r = 0, len(arr)-1
    while l<=r:
        p = (l+r)//2
        # [l1,2,3,4,3,2,r1]
        # [1,2,l3,4,p3,2,r1]
        # [1,l2,p3,4,r3,2,1]
        if arr[p] <= arr[l] and p != l:
            r = p - 1
        elif arr[p] <= arr[r] and p != r:
            l = p + 1
        elif arr[l] < arr[p] > arr[r]:
            l += 1
            r -= 1
        else:
            return p
    return p