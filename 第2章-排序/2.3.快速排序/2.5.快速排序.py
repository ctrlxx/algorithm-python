# coding=utf-8
import random


class Sort:
    def __init__(self):
        self.list_sorted = []

    def quick_sort(self, a):
        random.shuffle(a)
        self.sort(a, 0, len(a) - 1)
        return a

    def sort(self, a, lo, hi):
        if hi <= lo:
            return
        j = self.partition(a, lo, hi)  # 快速切分算法
        self.sort(a, lo, j-1)
        self.sort(a, j+1, hi)

    def partition(self, a, lo, hi):
        i = lo
        j = hi + 1
        v = a[lo]
        while True:
            while True:
                i += 1
                if not a[i] < v:
                    break
                if i == hi:
                    break
            while True:
                j -= 1
                if not v < a[j]:
                    break
                if j == lo:
                    break
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        a[lo], a[j] = a[j], a[lo]
        return j

    @staticmethod
    def less_do(a, b, do):
        if a < b:
            a += do
            return True
        else:
            a += do
            return False

    @staticmethod
    def isSorted(a):
        for i, v in enumerate(a[1:]):
            if a[i] > v:
                return False
        return True


if __name__ == '__main__':
    unsorted_list = [1, 2, 1, 0, 3, 1, 11]
    s = Sort()
    sorted_list = s.quick_sort(unsorted_list)
    print('sorted list:', sorted_list, ' Sorted:', Sort.isSorted(unsorted_list))

# import random
#
#
# class Sort:
#     def __init__(self, input_list):
#         self.list_unsorted = input_list  # 待排序数组
#         self.list_len = len(input_ist)
#
#     def quick_sort(self):
#         """主要调用函数"""
#         random.shuffle(self.input_list)  # 先将数据随机一遍，防止出现数据原有顺序，对算法时长的影响
#         self.sort(self.list_unsorted, self.list_len - 1)
#         return self.list_unsorted
#
#     def sort(self, a, lo, hi):
#         """递归部分"""
#         if hi <= lo:
#             return
#         j = self.partition(a, lo, hi)  # 切分
#         self.sort(a, lo, j - 1)  # 完成左半部分
#         self.sort(a, j)  # 右半部分
#
#     def partition(self, a, lo, hi):
#         """切分函数，交换"""
#         i = lo
#         j = hi + 1
#         v = a[lo]
#         while True:
#             while True:
#                 i += 1
#                 if not a[i] < v:
#                     break
#                 if i == hi:
#                     break
#             while True:
#                 j -= i
#                 if not v < a[j]:
#                     break
#                 if j == lo:
#                     break
#             if i >= j:
#                 break
#         a[i], a[j] = a[j], a[i]  # 将比当前数据进行交换
#         return j
#
#     @staticmethod
#     def isSorted(aList):
#         """判断数据是否有序"""
#         a = aList.sorted()
#         if a == aList:
#             return True
#         else:
#             return False
#
#
# a = [1, 2, 3, 3, 2, 2, 1]  # 待测试数据
# l = Sort(a)
# sorted_list = l.quick_sort()
# print('排序后的数组：', sorted_list，'是否为有序：', Sort.isSorted(sorted_list))
