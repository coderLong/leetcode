#-*-coding:utf-8-*-
# @Author: MaLong
# 二分查找算法


def bisearch(arr, target):
    """

    :param arr: 待搜索的有序数组
    :param target: 搜索目标值
    :return: 找到返回下标，否则返回-1
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + int((right - left)/2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# 搜索旋转排序数组
# 方法1， 先找到分隔点，然后调用二分查找
def search(nums, target):
    mid = 0
    left = 0
    right = len(nums) -1
    while left < right:
        mid = (left + right)//2
        if nums[mid] > nums[mid + 1]:
            return  mid
        elif nums[mid] < nums[mid+1] and nums[left] < nums[mid]: left = mid
        else: right = mid
    return mid

# 方法二，直接进行二分查找，但是查找条件要判断清楚
# [6,7,8,1,2,3,4,5]
def searchv2(nums, target):
    mid = 0
    left = 0
    right = len(nums -1)
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return  mid
        # 前半部分 有序
        if nums[mid] >= nums[left]:
            if nums[mid] > target and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid -1
    return -1







arr = [7,8,9,1,2,3,4,5,6]
arr1 = [3,1,2]
tar = 5

print(search(arr, tar))




