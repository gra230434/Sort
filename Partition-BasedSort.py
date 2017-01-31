def Insertsort(array, left, right):
    for pos in range(left, right+1):
        Insert(array, pos, array[pos])


def Insert(array, pos, value):
    tmp = pos - 1
    while tmp >= 0 and array[tmp] > value:
        array[tmp+1] = array[tmp]
        tmp = tmp - 1
    array[tmp+1] = value


def swap(sqc, i, j):
    sqc[i], sqc[j] = sqc[j], sqc[i]


def quicksortstart(lis):
    quicksort(lis, 0, len(lis)-1)


def quicksort(lis, left, right):
    minsize = 5
    if left < right and right - left > minsize:
        pivot = getpivot(lis, left, right)
        pivot = partition(lis, left, right, pivot)
        quicksort(lis, left, pivot-1)
        quicksort(lis, pivot+1, right)
    else:
        Insertsort(lis, left, right)


def getpivot(lis, left, right):
    mid = (right - left) // 2
    maxnum = lis[right]
    pivot = right
    if lis[left] > maxnum:
        maxnum = lis[left]
        pivot = left
    if lis[mid] > maxnum:
        maxnum = lis[mid]
        pivot = mid
    return pivot


def partition(lis, left, right, pivot):
    swap(lis, pivot, right)
    store = left
    for value in range(left, right-1):
        if lis[value] < lis[left]:
            swap(lis, value, store)
            store = store + 1
    swap(lis, right, store)
    return store


def main():
    sqc = [2, 7, 1, 40, 51, 32, 1, 95, 10]
    quicksortstart(sqc)
    print(sqc)


if __name__ == '__main__':
    main()
