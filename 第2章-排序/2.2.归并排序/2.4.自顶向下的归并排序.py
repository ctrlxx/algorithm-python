# # coding=utf-8
class Sort:
    def __init__(self, a=None):
        self.unsorted_list = a

    @staticmethod
    def merge(a, b):
        c = []
        h = j = 0
        while j < len(a) and h < len(b):
            if a[j] < b[h]:
                c.append(a[j])
                j += 1
            else:
                c.append(b[h])
                h += 1

        if j == len(a):
            for i in b[h:]:
                c.append(i)
        else:
            for i in a[j:]:
                c.append(i)

        return c

    def merge_sort(self, lists):
        if len(lists) <= 1:
            return lists
        middle = int(len(lists) / 2)
        left = self.merge_sort(lists[:middle])
        right = self.merge_sort(lists[middle:])
        return self.merge(left, right)

    @staticmethod
    def isSorted(a):
        for i, v in enumerate(a[1:]):
            if a[i] > v:
                return False
        return True


if __name__ == '__main__':
    unsorted_list = [1, 2, 13, 1, 11]
    s = Sort()
    sorted_list = s.merge_sort(unsorted_list)
    print('sorted list:', sorted_list, ' Sorted:', Sort.isSorted(sorted_list))
