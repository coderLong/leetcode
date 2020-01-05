# coding:utf-8
# 求x的N次方'''


def my_power(x, n):
    if n < 0:
        return 1.0/my_power(x,-n)
    if n == 0:
        return 1.0
    elif n % 2 == 0:
        half = my_power(x,n//2)
        return half*half
    else:
        half = my_power(x, n // 2)
        return half * half*x


print(my_power(2.0,10))