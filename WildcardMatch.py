__author__ = 'Jie'
"""
44. Wildcard Matching
Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dynamic programming.
        # first create a matrix for restoring all the previous results.
        # initialize
        # find the suitable relation function
        # return results
        rows,cols=len(s),len(p)
        dp=[[False]*(cols+1) for _ in range(rows+1)]
        # initialize
        dp[0][0]=True
        for col in range(1,cols+1):
            # initialize the first row when s is empty, but p from 0 to cols.
            # cols  and rows represent the numbers of characters in s and p, respectively.
            if p[col-1]=="*":
                dp[0][col]=dp[0][col-1]
        print (dp)
        #start to use dp
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                #case 1: e.g. s="abc";p="abc" or "ab?".
                if p[col-1]==s[row-1] or p[col-1]=="?":
                    dp[row][col]=dp[row-1][col-1]
                # case 2: e.g. s="abcd", p="ab*"; case 3:e.g. s="abcd", p="abcd**".
                elif p[col-1]=="*":
                    dp[row][col]=dp[row-1][col] or dp[row][col-1]
        print (dp)
        return dp[-1][-1]

solution=Solution()
# s="acdcb"
# p="a*c?b"
s = "adceb"
p = "*a*b"
ans=solution.isMatch(s,p)
print (ans)