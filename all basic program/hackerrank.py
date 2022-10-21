sum_list = []
sums = 0

for i in range(len(arr)):
    for j in arr:
        if arr.index(j) == i:
            continue
        else:
            sums += j
    sum_list.append(sums)
    sums = 0
