"""
49. Group Anagrams
Medium


Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import Counter, defaultdict
from typing import List


def groupAnagrams(strs):
    memo = defaultdict(list)
    res = list()
    for i in range(len(strs)):
        s = strs[i]
        k = sorted(Counter(s).items())
        sk = str(k)
        memo[sk].append(s)
    for _, v in memo.items():
        res.append(v)
    return res

def groupAnagrams_0(strs: List[str]) -> List[List[str]]:
    dic = dict()
    for i in range(len(strs)):
        key = tuple(sorted(strs[i]))
        if key in dic:
            dic[key].append(strs[i])
        else:
            # dic.update({key:list()})
            # dic[key].append(strs[i])
            dic[key] = [strs[i]]
    return dic.values()