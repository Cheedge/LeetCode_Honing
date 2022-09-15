"""
2007. Find Original Array From Doubled Array
Medium

An integer array original is transformed into a doubled array changed
by appending twice the value of every element in original,
and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array.
If changed is not a doubled array, return an empty array.
The elements in original may be returned in any order.


Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.


Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105
"""
from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # TLE
        # changed.sort(reverse=True)
        # res = list()
        # while changed:
        #     it = changed.pop()
        #     if it*2 in changed:
        #         changed.remove(it*2)
        #         res.append(it)
        #     else:
        #         return []
        # return res
        changed.sort(reverse=True)
        # cnt = OrderedDict()
        # cnt = defaultdict(int)
        # for it in changed:
        #     cnt[it] += 1
        # res = list()
        cnt, res = Counter(changed), list()
        if 0 in cnt:
            nm = cnt[0]
            if cnt[0] % 2 != 0:
                return []
            else:
                cnt.pop(0)
                res.extend([0] * (nm // 2))
        while cnt:
            k, v = cnt.popitem()
            if 2 * k in cnt:
                if cnt[2 * k] == v:
                    cnt.pop(2 * k)
                elif cnt[2 * k] > v:
                    cnt[2 * k] -= v
                else:
                    return []
                # res.append(k)
                res.extend([k] * v)
            else:
                # print(k, v)
                return []
        return res
