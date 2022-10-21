data2 = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	d = int(input(f"enter the index of {i}: "))

	data2.append(d)

def counting(a):

	actual_size = len(a)

	size = max(a)

	count = [0] * (size +1)

	out = [0] * actual_size

	for i in range(0,actual_size):
		count[a[i]] += 1


	for i in range(1, len(count)):
		count[i] += count[i-1]

	i = actual_size - 1
	while i >= 0:
		out[count[a[i]] - 1] = a[i]
		count[a[i]] -= 1
		i -= 1

	return out


ans = counting(data2)

print(ans)
