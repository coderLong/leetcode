#-*-coding:utf-8-*-
# @Author: MaLong

# three sum 三个数相加

def three_sum(nums):
    res = []
    # 建立字典, value 是下标
    hash_sum = {}
    for i in range(len(nums)):
        key = 0 - nums[i]
        if key not in hash_sum:
            hash_sum[key] = [i]
        else:
            tmp = hash_sum[key]
            tmp.append(i)
            hash_sum[key] = tmp
    print(hash_sum)

    # 做两两组合的循环
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums), 1):
            if (nums[i] + nums[j]) in hash_sum:
                idxs = hash_sum[nums[i] + nums[j]]
                for id in idxs:
                    if id != i and id != j:
                        print(([i,j,id]))
                        res.append([nums[i], nums[j], nums[id]])
    return  res

# 有效的括号 https://leetcode-cn.com/problems/valid-parentheses
def isValid( s):
    """
    :type s: str
    :rtype: bool
    """

# 28. 实现 strStr()
def sunday(s,t):
    '''
    字符串查找算法 sunday 算法
    :param s: 主串
    :param t: 模板串
    :return: 找到返回下标，找不到返回 -1
    '''
    move_step = {}
    t_len = len(t)
    for k in range(t_len):
        move_step[t[k]] = t_len - k
    i = 0

    while i <= len(s) - t_len:
        flag = True
        for j in range(t_len):
            if t[j] != s[i + j]:
                flag = False
                if i + t_len < len(s):
                    next_char = s[i+t_len]
                    if next_char in move_step:
                        i = i + move_step[next_char]
                    else:
                        i = i + t_len + 1
                else:
                    return -1
                break
        if flag:
            return i
    return -1










if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    t = 'substring searjch'
    s = 'search'
    #print(s.index(t))
    print(sunday(s=s,t=t))



