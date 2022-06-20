"""
1385. Find the Distance Value Between Two Arrays
Easy

Given two integer arrays arr1 and arr2, and the integer d, 
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that 
there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
 

Constraints:

1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100
"""
def findTheDistanceValue(arr1, arr2, d):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type d: int
    :rtype: int
    """
    # loop over arr1
    n1, n2 = len(arr1), len(arr2)
    arr2.sort()
    ans = 0
    for i in range(n1):
        l, r = 0, n2-1
        while l<=r:
            m = (l+r)//2
            # find insert arr1[i] place
            # [5,8,9,10] 4
            #  0 1 2  3
            if arr1[i] > arr2[m]:
                # print("l", l, arr1[i])
                l = m + 1
            elif arr1[i] < arr2[m]:
                # print("r",r, arr1[i])
                r = m - 1
            else:
                if d >= 0:
                    break
        # in case len(arr2)=1 eg. [10]
        if m - 1 < 0 and m + 1 < n2:
            res = min(abs(arr2[m+1]-arr1[i]), abs(arr2[m]-arr1[i]))
        elif m + 1 >= n2:
            res = min(abs(arr2[m-1]-arr1[i]), abs(arr2[m]-arr1[i]))
        else:
            res = min(abs(arr2[m+1]-arr1[i]), abs(arr2[m]-arr1[i]), abs(arr2[m-1]-arr1[i]))
        if res > d:
            ans += 1
    return ans