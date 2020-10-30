def max2(a, b):
    if bool(int(a/b)):
        return a
    elif bool(int(b/b)):
        return b


def partition(array, l, h):
    x = array[h]
    i = l - 1
    for j in range(l, h):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[h] = array[h], array[i+1]
    return i+1


def fSelect(list, index):
    return fSelect_helper(list, index, 0, len(list) - 1)


def fSelect_helper(list, index, l, h):
    if l == h:
        return list[l]
    
    partition_i = partition(list, l, h)
    if index < partition_i:
        return fSelect_helper(list, l, h-1, index)
    elif index == partition_i:
        return list[index]
    else:
        return fSelect_helper(list, l+1, h, index)


def main():
#    print(max2(5, 10))
    print(fSelect([3, 2, 1], 2))


if __name__ == "__main__":
    main()