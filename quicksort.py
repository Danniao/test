# _*_ coding:utf-8 _*-
# 作者：aden
# @time:2022/3/29 0029
# @Email:f1500867251@126.com
# @File:quicksort.py
def quickSort(arr):
    if len(arr) < 2:  # 基线条件：为空或者只包含一个元素的数组是“有序”的
        return arr
    else:
        pivot = arr[0]  # 递归条件
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        # return quickSort(less) + [pivot] + quickSort(greater)
        return quickSort(greater) + [pivot] + quickSort(less)


print(quickSort([10, 25, 2, 3]))