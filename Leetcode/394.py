"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is:
    k[encoded_string], where the encoded_string inside the square brackets
    is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        # digit: combined to one number eg."32" -> stack
        # "]": pop out all prev till "["
        # next pop out digit number
        # tmp = "".join("str")*times
        # append tmp to stack
        # after all loop over stack
        # res += items
        stack, res, n = list(), "", len(s)       
        i = 0
        while i<n:
            # print(f"{res=}, {stack=}, {i=}, {s[i]=}")
            if s[i].isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(num)
            elif s[i] == ']':
                tmp = ''
                j = -1
                while stack[j] != '[':
                    tmps = stack.pop()
                    tmp = tmps + tmp
                    # j -= 1
                # pop out '['
                stack.pop()
                times = stack.pop()
                # res += tmp * int(times)
                stack.append(tmp * int(times))
                i += 1
            else:
                stack.append(s[i])
                i += 1
        # print(stack)
        for it in stack:
            res += it
        return res