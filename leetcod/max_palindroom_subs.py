#-*-coding:utf-8-*-
# @Author: MaLong
import numpy as np


# 动态规划算法，初始状态，状态转移方程

def longestPalindrome( s):
    s_len = len(s)
    if s_len == 0:
        return  s

    dp = np.zeros((s_len,s_len))
    max_len = 1
    start = 0
    for i in range(s_len):
        dp[i][i] = 1
        if i+1 <= s_len -1 and s[i] == s[i+1]:
            dp[i][i+1] = 1
            max_len = 2
            start = i
    for l in range(3, s_len + 1,1):
        for i in range(0, s_len - l + 1,1):
            j = i + l  -1
            if s[i] == s[j] and dp[i+1][j-1] == 1:
                dp[i][j] = 1
                start = i
                max_len = l

    return s[start:start + max_len]

print(longestPalindrome(''))
