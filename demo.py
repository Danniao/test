# _*_ coding:utf-8 _*-
# 作者：aden
# @time:2022/3/29 0029
# @Email:f1500867251@126.com
# @File:demo.py
def binarySearch(list, item):
    low = 0
    high = len(list) - 1  # 索引值
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [64, 34, 25, 12, 22, 11, 90]

print(binarySearch(my_list, 6))