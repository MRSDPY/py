import numpy as n
str1 = input("Enter 1st string : ")
str2 = input("Enter 2st string : ")


def lcs():
    a = len(str1)
    b = len(str2)

    table = n.zeros((a+1, b+1))

    for i in range(a+1):
        for j in range(b+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i - 1][j - 1]+1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    i = a
    j = b
    final_list = [''] * (int(table[a][b]))
    index = int(table[a][b])
    while i >= 0 and j >= 0:
        if str1[i-1] == str2[j-1]:
            final_list[index - 1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("Length is :", table[a][b], "\n")
    print("longest common subsequence is : ", final_list, "\n")
    print("Table : ", "\n", table)


lcs()
