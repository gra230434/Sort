def sort(array):
    for pos in range(1, len(array)):
        Insert(array, pos, array[pos])


def Insert(array, pos, value):
    tmp = pos - 1
    while tmp >= 0 and array[tmp] > value:
        array[tmp+1] = array[tmp]
        tmp = tmp - 1
    array[tmp+1] = value
    pass


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
    sort(array)
    print(array)


if __name__ == '__main__':
    main()
