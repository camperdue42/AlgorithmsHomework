import math

def search(array, value):
    final = False
    end = len(array) - 1
    start = 0
    while start <= end:
        middle = start + math.floor((end - start) / 2)
        if value == array[middle]:
            final = True
            break
        elif value < array[middle]:
            end = middle - 1
        elif value > array[middle]:
            start = middle + 1
        else:
            print("something has gone horribly wrong")
    return final


def sorted_has_sum(S, x):
    array = S
    result = False
    for n in S:
        looking_for = x - n
        if search(array, looking_for):
            result = True
            break
        else:
            array = array[1:]
    return result


def partition(array, l, h):
    x = array[h]
    i = l - 1
    for j in range(l, h):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[i+1], array[h] = array[h], array[i+1]
    return i+1


def quicksort_recursive(a):
    quicksort_recursive_helper(a, 0, len(a) - 1)


def quicksort_recursive_helper(a, l, h):
    if l < h:
        m = partition(a, l, h)
        quicksort_recursive_helper(a, l, m-1)
        quicksort_recursive_helper(a, m+1, h)


def main():
    print(search([1, 2, 3, 6, 10], 11))
    print(sorted_has_sum([1, 2, 5], 6))


if __name__ == "__main__":
    main()