data2 = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	d = int(input(f"enter the index of {i}: "))

	data2.append(d)

def mergeSort(a):
	if len(a) == 1:
		return

	mid = len(a) // 2

	left = a[:mid]
	rigth = a[mid:]

	mergeSort(left)
	mergeSort(rigth)

	p1 = p2 = k = 0

	while p1 < len(left) and p2 < len(rigth):
		if left[p1] < rigth[p2]:
			a[k] = left[p1]
			p1 += 1
		else:
			a[k] = rigth[p2]
			p2 += 1

		k += 1

	while p1<len(left):
		a[k] = left[p1]
		p1 += 1
		k += 1

	while p2<len(rigth):
		a[k] = rigth[p2]
		p2 += 1
		k += 1

	return a

d = mergeSort(data2)

print(d)