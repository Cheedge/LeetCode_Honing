"""
1309. Decrypt String from Alphabet to Integer Mapping
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!python的for loop在loop内i 是无法更改的!!!!!!!!!!!!!!!!!!!!!!!!!!

Easy

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters 
as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
 

Constraints:

1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.
"""
def freqAlphabets(s: str) -> str:
    res = list()
    i = len(s)-1
    while i>=0:
        # print(i)
        if s[i] == '#':
            res.append(chr(int(s[i-2:i])+96))
            i -= 2
            # print(i,"++++++++++")
        else:
            # print(i, s[i], "_________")
            res.append(chr(int(s[i])+96))
        i -= 1
    ans = str()
    for i in range(len(res)-1, -1, -1):
        ans += res[i]
    return ans