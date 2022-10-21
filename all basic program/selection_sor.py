data2 = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	d = int(input(f"enter the index of {i}: "))

	data2.append(d)


def selection():
	for i in range(len(data2)):
		minIndex = i
		for j in range(i + 1, len(data2)):
			if data2[j] < data2[minIndex]:
				minIndex = j

		if minIndex != i:
			data2[i], data2[minIndex] = data2[minIndex], data2[i]

	print(data2)

selection()
