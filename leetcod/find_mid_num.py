#-*-coding:utf-8-*-
# @Author: MaLong
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 寻找两个有序数组的中位数
# 更一般化，寻找两个有序数组中第K大的数字
'''
arr1, arr2 , k
若arr1[k/2 -1 ] == arr2[k/2 -1 ]  return arr1[k/2 -1]
若arr1[k/2-1] > arr2[k/2 - 1], arr2 里面的前 k/2 - 1 个数字一定在排序后的前k个数字中
更新数组查找开始地址，k也更新
若arr1[k/2-1] < arr2[k/2 -1]
则 arr1[k/2 -1] 可以不再考虑
这样每次去掉k/2个数字，直到k=1
'''

def find_kth(arr1, arr2, k):
    # 假设 arr1 长度 <= len(arr2)
    if len(arr2) < len(arr1):
        return find_kth(arr2, arr1, k)


    if len(arr1) == 0:
        return arr2[k-1]

    if k == 1:
        return  min(arr1[0], arr2[0])

    mid = int(k/2)

    if arr1[mid] ==





a = [2,3,4]
b = [3,4,5,6]
print(findKth(a,0,b,0,4))
