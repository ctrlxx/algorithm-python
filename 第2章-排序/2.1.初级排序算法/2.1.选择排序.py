# # coding=utf-8
class Sort:
    def __init__(self):
        self.list_sorted = []

    @staticmethod
    def selection(a):
        n = len(a)
        for i in range(n):
            Min = i
            for j in range(n):
                if a[j] > a[Min]:
                    Min = j
                a[i], a[Min] = a[Min], a[i]

    @staticmethod
    def isSorted(a):
        for i, v in enumerate(a[1:]):
            if a[i] > v:
                return False
        return True


if __name__ == '__main__':
    unsorted_list = [1, 2, 3, 1, 11]
    Sort.selection(unsorted_list)
    print('sorted list:', unsorted_list, ' Sorted:', Sort.isSorted(unsorted_list))
