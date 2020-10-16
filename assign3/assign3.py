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


def has_sum(S, x):
    sorted_s = quicksort_iterative(S)
    return sorted_has_sum(sorted_s, x)


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


def quicksort_iterative(a):
    l = 0
    h = len(a) - 1
    stack = [None] * ((h - l) + 1)
    top = 0

    stack[top] = l
    top += 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        m = partition(a, l, h)

        if m - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = m - 1

        if m + 1 < h:
            top += 1
            stack[top] = m + 1
            top += 1
            stack[top] = h

    return a


def main():
#     print(search([1, 2, 3, 6, 10], 11))
#     print(sorted_has_sum([1, 2, 5], 6))
#     print(quicksort_iterative([10, 5, 1, 7, 8, 2, 10]))
#     print(has_sum([1, 2, 5], 10)) this is what is meant by okay to use one number in S twice I'm assuming (?)
# print(has_sum([1, 2, 5], 11))


# if __name__ == "__main__":
#     main()