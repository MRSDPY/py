n_p = int(input("how many items are there : "))

print("\n Enter the weight of all that items..")

weight = [int(input(f"Enter weight of item {i} : ")) for i in range(n_p)]

print("\n Enter the profit for all that items..")

profit = [int(input(f"Enter profit for item {i} : ")) for i in range(n_p)]

W = int(input("\n Enter the knapsack weight : "))


ratio = [(profit[i] / weight[i]) for i in range(n_p)]

weight = [w for _,w in sorted(zip(ratio, weight), reverse=True)]

profit = [p for _,p in sorted(zip(ratio, profit), reverse=True)]


def knapsack(weight, profit, ratio):

	pick_item = [0 for i in range(n_p)]

	in_weight = 0

	for i in range(n_p):

		if in_weight + weight[i] <= W:
			pick_item[i] = 1
			in_weight += weight[i]
		else:
			pick_item[i] = (W - in_weight) / weight[i]
			weight = W
			break

	final_profit = [(profit[i] * pick_item[i]) for i in range(n_p)]

	ans = {
		"total_profit": sum(final_profit),
		"pick_item": pick_item,
	}

	return ans


pro = knapsack(weight, profit, ratio)

for i, v in pro.items():
	print(f"{i} -> {v}")

