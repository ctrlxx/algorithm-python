# coding=utf-8


class Sort:
    def __init__(self):
        self.list_unsorted = []

    def heap_sort(self, L):
        L_length = len(L) - 1

        first_sort_count = L_length // 2
        for i in range(first_sort_count):
            self.heap_adjust(L, first_sort_count - i, L_length)

        for i in range(L_length - 1):
            L = self.swap_param(L, 1, L_length - i)
            self.heap_adjust(L, 1, L_length - i - 1)

        return [L[i] for i in range(1, len(L))]

    @staticmethod
    def heap_adjust(L, start, end):
        temp = L[start]

        i = start
        j = 2 * i

        while j <= end:
            if (j < end) and (L[j] < L[j + 1]):
                j += 1
            if temp < L[j]:
                L[i] = L[j]
                i = j
                j = 2 * i
            else:
                break
        L[i] = temp

    @staticmethod
    def swap_param(L, i, j):
        L[i], L[j] = L[j], L[i]
        return L

    @staticmethod
    def isSorted(a):
        for i, v in enumerate(a[1:]):
            if a[i] > v:
                return False
        return True


if __name__ == '__main__':
    unsorted_list = [1, 2, 1, 0, 3, 1, 11]
    s = Sort()
    sorted_list = s.heap_sort(unsorted_list)
    print('sorted list:', sorted_list, ' Sorted:', Sort.isSorted(sorted_list))
