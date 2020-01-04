#-*-coding:utf-8-*-
# @Author: MaLong
# 全排列

res = []
def permute(nums, trace):
    if len(nums) == len(trace):
        tmp = trace.copy()
        res.append(tmp)
        return
    for i in range(len(nums)):
        if nums[i] in trace:
            continue
        trace.append(nums[i])
        permute(nums, trace)
        trace.pop()

a = [1,2,3]
permute(a, [])
print(res)


