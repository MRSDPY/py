T = int(input("Enter The Number Of Testcase: "))

dic = []
max_dic = {}
min_dic = {}
count = 0

for t in range(T):
	dic.append([])
	N = int(input(f"Enter {t}th test case person: "))
	for n in range(N):
		dic[t].append(int(input("Enter The Person Distance: ")))

for t in range(T):
	for n in range(len(dic[t])-1):
		if abs(dic[t][n] - dic[t][n + 1]) <= 2:
			count += 1
		elif len(dic[t]) <= 2 and abs(dic[t][n] - dic[t][n + 1]) > 2:
			break
		elif abs(dic[t][n] - dic[t][n + 1]) > 2:
			count += 1
			break
	max_dic[t] = count+1
	count = 0

for t in range(T):
	for n in range(len(dic[t])-1):
		if abs(dic[t][n] - dic[t][n + 1]) > 2:
			break
		elif len(dic[t]) <= 2 and abs(dic[t][n] - dic[t][n + 1]) > 2:
			count += 1
		else:
			count += 1
	min_dic[t] = count+1
	count = 0

for f in range(len(min_dic)):
	print(f"{min_dic[f]} {max_dic[f]}")