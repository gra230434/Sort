def selectsort(array):
    for i in range(len(array)-1, 0, -1):
        ind = findthebiggest(i, array)
        array[ind], array[i] = array[i], array[ind]
    return array


def findthebiggest(to, array):
    val = -1
    ind = -1
    for i in range(0, to):
        if val < array[i]:
            val = array[i]
            ind = i
    return ind


def strtoint(array):
    for pos in range(len(array)):
        array[pos] = int(array[pos])


def inputarray():
    array = input("array > ")
    array = array.split()
    strtoint(array)
    return array


def main():
    array = inputarray()
    array = selectsort(array)
    print(array)


if __name__ == '__main__':
    main()
