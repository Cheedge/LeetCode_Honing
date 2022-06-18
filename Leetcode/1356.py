"""
1356. Sort Integers by The Number of 1 Bits
Easy

You are given an integer array arr. 
Sort the integers in the array in ascending order by the number of 1's in their binary representation 
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

 

Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation,
you should just sort them in ascending order.
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 104
"""
import pytest


def sortByBits(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    from collections import defaultdict
    d = defaultdict(list)
    
    for it in arr:
        # bin(10) -> '0b1010' -> '101' -> ['', '']
        s = len(bin(it).strip('0b').split('1')) - 1
        # defaultdict can auto sort: only in python2!!!!!!!!!!!!!
        print(it, s, d)
        d[s].append(it)
    res = list()
    # in python3 should add this sorted() to sort dictionary!!!
    for _, v in sorted(d.items()):
        # if v:
        v.sort()
        res.extend(v)
    return res

test_case = [
    ([0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7]),
    ([1024,512,256,128,64,32,16,8,4,2,1],[1,2,4,8,16,32,64,128,256,512,1024]),
    ([32,23,1,245,2345,654,6,2,699], [1,2,32,6,23,654,2345,245,699]),
]

@pytest.mark.parametrize("arr, expect", test_case)
def test_sortByBits(arr, expect):
    assert sortByBits(arr) == expect