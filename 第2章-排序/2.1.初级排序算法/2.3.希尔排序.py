# # # coding=utf-8
# class Sort:
#     def __init__(self):
#         self.list_sorted = []
#
#     def shell(self, a):
#         n = len(a)
#         gap = n // 2
#         while gap > 0:
#             for i in range(gap):
#                 self.gapInsetionSort(a, i, gap)
#             gap = gap // 2
#         return a
#
#     @staticmethod
#     def gapInsetionSort(alist, start_pos, gap):
#         # 希尔排序的辅助函数
#         for i in range(start_pos + gap, len(alist), gap):
#             position = i
#             current_value = alist[i]
#
#             while position > start_pos and alist[position - gap] > current_value:
#                 alist[position] = alist[position - gap]
#                 position = position - gap
#             alist[position] = current_value
#
#     @staticmethod
#     def isSorted(a):
#         for i, v in enumerate(a[1:]):
#             if a[i] > v:
#                 return False
#         return True
#
#
# if __name__ == '__main__':
#     unsorted_list = [1, 2, 13, 1, 11]
#     s = Sort()
#     sorted_list = s.shell(unsorted_list)
#     print('sorted list:', sorted_list, ' Sorted:', Sort.isSorted(unsorted_list))
