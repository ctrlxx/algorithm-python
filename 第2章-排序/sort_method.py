import sys
import datetime
from random import randint


def generateRandomArray(n, lo, hi):
    arr = [randint(lo, hi) for x in range(n)]
    return arr


def generateNearlyOrderedArray(n, swapTimes):
    arr = []
    for i in range(n):
        arr.append(i)
    for j in range(swapTimes):
        posx = randint(0, n - 1)
        posy = randint(0, n - 1)
        arr[posx], arr[posy] = arr[posy], arr[posx]
    return arr


def isSorted(alist):
    for i in range(0, len(alist) - 1):
        if alist[i] > alist[i + 1]:
            return False
        return True


# 冒泡排序
def bubbleSort(alist):
    n = len(alist)
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


# 冒泡排序-优化
def bubbleSort_2(alist):
    n = len(alist)
    exchange = False
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                exchange = True
        # 如果发现整个排序过程中没有交换，提前结束
        if not exchange:
            break
    return alist


# 选择排序
def selectionSort(alist):
    n = len(alist)

    for i in range(n - 1):
        # 寻找[i,n]区间里的最小值
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


# 插入排序
def insertionSort(blist):
    n = len(blist)
    for i in range(1, n):
        # 寻找a[i]合适的插入位置
        temp = blist[i]
        for j in range(i, 0, -1):
            if temp < blist[j - 1]:
                blist[j] = blist[j - 1]
            else:
                break
        blist[j - 1] = temp
    return blist


# 希尔排序
def shellSort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap):
            gapInsetionSort(alist, i, gap)
        gap = gap // 2
    return alist


# start子数列开始的起始位置， gap表示间隔
def gapInsetionSort(alist, startpos, gap):
    # 希尔排序的辅助函数
    for i in range(startpos + gap, len(alist), gap):
        position = i
        currentvalue = alist[i]

        while position > startpos and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


# 堆排序
def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


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


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length // 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


def testSort(func, alist):
    start = datetime.datetime.now()
    alist = func(alist)
    end = datetime.datetime.now()
    print('heap_sort：%s s' % (end - start).total_seconds())
    print("Sorted list: %s" % alist)
    assert isSorted(alist), "排序算法错误\n"


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    result = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        alist = list(map(int, line.split()))
        testSort(heap_sort, alist)

