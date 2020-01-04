#-*-coding:utf-8-*-
# @Author: MaLong

# 判断一个数字是否为回文数字
def isPalindrome(x):
    if x < 0 or (x%10 == 0 & x!= 0):
        return False
    div = 1
    while x //div >1:
        div = div * 10

    while x > 0:
        first = x // div
        last = x % 10
        if first != last:
            return False

        x = x % div
        x = x // 10
        div = div // 100
    return True


print(isPalindrome(10111))
