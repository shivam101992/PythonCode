#uses python3
import sys
def knapsack_01(total,weights,values):
    total_items = len(weights)

    rows = total_items + 1
    cols = total + 1

    T = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i - 1]:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = max(T[i - 1][j], values[i - 1] + T[i - 1][j - weights[i - 1]])

    return T[rows - 1][cols -1]

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = knapsack_01(capacity, weights, values)
    print("{:.4f}".format(opt_value))   