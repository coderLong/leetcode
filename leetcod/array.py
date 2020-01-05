# coding:utf-8
# 数组相关的算法

# 旋转打印矩阵


import numpy as np


def transferMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = []
    for i in range((m-1)//2 + 1):  # 条件限定错误， 需要 a1,c1, a2,c2
        for j in range(i,n-i):  # 向右
            ans.append(matrix[i][j])
        for j in range(i+1, m-i):  # 向下, 固定了列 n-i-1
            ans.append(matrix[j][n-i-1])
        if m -i -1 > i:
            for j in range(n-i-2,i-1,-1):   # 向左, 固定了行 m-i-1
                ans.append(matrix[m-i-1][j])
        if n-i-1 > i:
            for j in range(m-i-2, i, -1):  # 向上， 固定列  i
                ans.append(matrix[j][i])

    return ans



# 合并区间


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x : x[0])  # 按照每个区间的开头排序
    ans = []
    if len(intervals) > 0:
        ans.append(intervals[0])
        for k in range(1, len(intervals)):
            left_part = ans[-1]
            right_part = intervals[k]
            if right_part[0] > left_part[1]:  # 完全没有交叉
                ans.append(right_part)
            else:
                new_part_left = min(left_part[0], right_part[0])
                new_part_right = max(left_part[1], right_part[1])
                ans[-1] = [new_part_left, new_part_right]
    return ans


# 旋转矩阵II


def transferMatrixII(n):
    import numpy as np
    ans = np.zeros(shape=[n, n],dtype=int)
    a1 = 0
    c1 = 0
    a2 = n-1
    c2 = n-1

    k = 1
    while k <= n*n:
        for i in range(c1, c2+1):
            ans[a1][i] = k
            k += 1

        for i in range(a1+1, a2+1):
            ans[i][c2] = k
            k += 1

        for i in range(c2 - 1, c1-1, -1):
            ans[a2][i] = k
            k += 1
        for i in range(a2-1,a1,-1):
            ans[i][c1] =k
            k += 1
        a1 += 1
        c1 += 1
        a2 -= 1
        c2 -= 1
    return ans.tolist()







n = 5
print(transferMatrixII(n))

#
# matrix = np.random.randint(0,10,(4,1))
# print(matrix)
# b = matrix.tolist()
# print(b)
# ans = transferMatrix(b)
# print(ans)
#
# a = [[1,3],[3,6],[8,10],[15,18]]
# print(merge(a))
