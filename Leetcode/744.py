"""
744. Find Smallest Letter Greater Than Target
Easy
￼
1783
￼
1640
￼
Add to List
￼
Share
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
 

Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.

"""
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    l, r = 0, len(letters)-1
    if letters[-1]<=target: return letters[0]
    while l<=r:
        m = (l+r)//2
        if letters[m] > target:
            r = m - 1
        elif letters[m] <= target:
            if letters[m+1] > target >= letters[m]:
                return letters[m + 1]
            else:
                l = m + 1
    return letters[l]