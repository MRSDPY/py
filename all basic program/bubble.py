data2 = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
	d = int(input(f"enter the index of {i}: "))

	data2.append(d)



def bubble():
	for i in range(len(data2)-1):
		for j in range(0, len(data2) - i - 1):
			if data2[j] > data2[j + 1]:
				data2[j], data2[j + 1] = data2[j + 1], data2[j]

	print(data2)

bubble()
