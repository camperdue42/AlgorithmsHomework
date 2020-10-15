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


def main():
    print(search([1, 2, 3, 6, 10], 11))


if __name__ == "__main__":
    main()