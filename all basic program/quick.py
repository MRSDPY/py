a = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	d = int(input(f"enter the index of {i}: "))

	a.append(d)


def partition(a, l, h):
	i = l - 1

	pivot = a[h]

	for j in range(l, h, 1):
		if a[j] <= pivot:
			i += 1
			a[i], a[j] = a[j], a[i]
		
	a[h], a[i+1] = a[i+1], a[h]

	return i+1

def quick(a, l, h):

	if l >= h:
		return

	pivot = partition(a, l, h)

	quick(a, l, pivot-1)

	quick(a, pivot+1, h)


quick(a, 0, len(a)-1)

print("final array :- ", a)