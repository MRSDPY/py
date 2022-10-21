data2 = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    d = int(input(f"enter the index of {i}: "))

    data2.append(d)


def insertion_sort(a):
    if len(a) == 1:
        return a

    for i in range(1, len(a)):
        j = i
        key = a[i]
        while j > 0 and a[j - 1] > key:
            a[j] = a[j - 1]
            j -= 1
        a[j] = key
    return a


ans = insertion_sort(data2)

print(ans)
