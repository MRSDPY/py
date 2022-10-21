# def partition(a,l,h):
# 	pivot = a[l]
# 	i= l
# 	j = h

# 	while i < j:

# 		while a[i] < pivot and i < h:
# 			i += 1
# 		while a[j] > pivot and j >= l:
# 			j -= 1
# 		if i < j:
# 			a[i], a[j] = a[j], a[i]

# 	a[j], a[l] = a[l], a[j]

# 	return j


# def quick(a,l,h):

# 	if l >= h:
# 		return

# 	pivot = partition(a, l, h)
# 	quick(a,l,pivot-1)
# 	quick(a,pivot+1, h)


# a = [2,34,4,6,3,23,4,2,56,3423,2454562,-2343.5456,6]

# quick(a, 0, len(a)-1)

# print(a)


# print("yg")
# def f(n):
# 	return(n*f(n-1))

# f(4)

# print(set("abac"))

# import numpy as np
# import pandas as pd

# s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

# print(s[s.isna()])

# help()

# import re


# phone_no = "+1-9904554170"

# pattern = re.compile(r"^\+\d{1,3}(\s|\-)(\d{10})$")

# match_str = pattern.match(phone_no).group()

# print(match_str)

# email_pa = re.compile(r"^[\w+][a-zA-Z0-9._-]+\@[a-z0-9.]+\.[a-z]{2,}$")

# try:
# 	match_em = email_pa.match(input("Enter Email : ")).group()
# 	print(match_em)
# except:
# 	print("Entered Email is not valid.")

list_ = [2, 12, 11, 7]
tar = 9

for i in range(0, len(list_) - 1):
	for j in range(0, len(list_)):
		if(list_[i] + list_[j] == tar):
			print(list([i, i+1]))
			break

