def fibDyn(n):
    dynamic = [0 for i in range(n)]
    dynamic[0] = 0
    dynamic[1] = 1
    for index in range(2, n):
        dynamic[index] = dynamic[index - 1] + dynamic[index - 2]
    return dynamic[n-1]


def knapsack(items, capacity):
    amount_of_items = len(items)
    dynamic = [[0 for i in range(capacity + 1)] for i in range(amount_of_items + 1)]
    for i in range(amount_of_items + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dynamic[i][j] = 0
            elif items[i][0] <= j:
                dynamic[i][j] = max(items[i-1][1] + dynamic[i-1][j-items[i-1][0]], dynamic[i-1][j])
            else:
                dynamic[i][j] = dynamic[i-1][j]
    return dynamic[amount_of_items][capacity]


def main():
    print(fibDyn(4))


if __name__ == "__main__":
    main()