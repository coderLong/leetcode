# coding:utf-8

# 不同路径 https://leetcode-cn.com/problems/unique-paths
def uniquePaths( m, n):
    import numpy as np
    paths = np.ones(shape=[m, n], dtype=int)
    a, c = 1, 1
    while a < m and c < n:
        for i in range(c, n):
            paths[a][i] = paths[a][i-1] + paths[a-1][i]
        for i in range(a+1, m):
            paths[i][c] = paths[i-1][c] + paths[i][c-1]
        a += 1
        c += 1
    print(paths)
    return paths[m-1][n-1]



# 最小编辑距离

def minLvdistance(s1, s2):



print(uniquePaths(1, 2))