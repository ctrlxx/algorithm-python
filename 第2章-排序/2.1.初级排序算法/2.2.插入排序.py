# # coding=utf-8
class Sort:
    def __init__(self):
        self.list_sorted = []

    @staticmethod
    def insertion(a):
        n = len(a)
        for i in range(1, n):
            # 寻找a[i]合适的插入位置
            temp = a[i]
            for j in range(i, 0, -1):
                if temp < a[j - 1]:
                    a[j] = a[j - 1]
                else:
                    break
                a[j - 1] = temp
        return a

    @staticmethod
    def isSorted(a):
        for i, v in enumerate(a[1:]):
            if a[i] > v:
                return False
        return True


if __name__ == '__main__':
    unsorted_list = [1, 2, 13, 1, 11]
    s = Sort()
    sorted_list = s.insertion(unsorted_list)
    print('sorted list:', sorted_list, ' Sorted:', Sort.isSorted(unsorted_list))
from collections import deque