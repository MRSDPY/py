def partition(a, l, h):
	pivot = (l+h)//2

	a[pivot], a[h] = a[h], a[pivot]

	i = l

	for j in range(l, h):
		if a[j] <= a[h]:
			a[i], a[j] = a[j], a[i]
			i += 1
			
	a[h], a[i] = a[i], a[h]

	return i

def quick(a, l, h):
	if l >= h:
		return

	pi = partition(a, l, h)

	quick(a, l, pi-1)

	quick(a, pi+1, h)


a = [12,45,7,8,1,1,0,-34, -23]

quick(a, 0, len(a)-1)

print(a)
