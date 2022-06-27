"""
557. Reverse Words in a String III
Easy
Given a string s, reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.


Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""
def reverseWords(s):
    return ' '.join(x[::-1] for x in s.split())


def reverse(s: str)->str:
    l, r = 0, len(s)-1
    sl = list(s)
    while l<r:
        sl[l], sl[r] = sl[r], sl[l]
        l += 1
        r -= 1
    # print(s)
    return "".join(it for it in sl)

def reverseWords2(self, s: str) -> str:
    lp, rp = 0, 0
    res = list()
    while rp<len(s):
        if s[rp] == ' ':
            # do reverse
            res.append(self.reverse(s[lp:rp]))#注意切片是左闭右开
            lp = rp + 1
        if rp ==len(s)-1:
            res.append(self.reverse(s[lp:rp+1]))#注意切片是左闭右开
            lp = rp + 1
        rp += 1
    return " ".join(it for it in res)