# _*_ coding:utf-8 _*-
# 作者：aden
# @time:2022/3/29 0029
# @Email:f1500867251@126.com
# @File:bubblesort.py
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]

bubblesort(arr)
print('排序后数组为：')
for i in range(len(arr)):
    print('%d' % arr[i])
