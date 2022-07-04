"""
139. Word Break
Medium

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[i]: before i, wether it canbe segemnet into words
        n = len(s)
        dp = [False for i in range(n)]
        i, j = 0, 0
        while i<n:
            # j += 1
            start = i
            end = i
            while start>=0:
                # print(s[start:end+1])
                if start == 0 and s[start:end+1] in wordDict:
                    dp[end] = True
                    if end>=n-1:
                        print(s[start:end+1])
                        return True
                if dp[start-1] and s[start:end+1] in wordDict:
                    # print(s[start:end+1])
                    dp[end] = True
                    if end>=n-1:
                        # print(start, end, dp[start],s[start:end+1])
                        return True
                start -= 1
            i += 1
        return False