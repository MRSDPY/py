import numpy as n

n_p = int(input("how many items are there : "))

print("\n Enter the weight of all that items..")

weight = [int(input(f"Enter weight of item {i} : ")) for i in range(n_p)]
# weight = sorted(weight)

print("\n Enter the profit for all that items..")

profit = [int(input(f"Enter profit for item {i} : ")) for i in range(n_p)]
# profit = sorted(profit)

W = int(input("\n Enter the knapsack weight : "))


def kn():
    table = n.zeros((n_p + 1, W + 1))

    for i in range(n_p + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i - 1] <= j:
                table[i][j] = max(profit[i - 1] + table[i - 1][j - weight[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    print("Table : \n", table, "\n")
    final_weight = [0] * n_p
    j = W
    i = n_p
    tm = 0
    print("\n Selected item index : ")
    while j > 0:
        if table[i][j] != table[i - 1][j]:
            final_weight[i - 1] = 1
            tm += weight[i - 1]
            j = j - weight[i - 1]
            i -= 1
            try:
                weight.index(j)
            except Exception as e:
                break
        else:
            i -= 1
    print(final_weight)
    print("\n Total Profit :")
    print(table[n_p][W])


kn()
