def sortFirst(l, condition):
	e = []
	o = []

	for i in l:
		if i % 2 == 0:
			e.append(i)
		else:
			o.append(i)

	if condition:
		return list(sorted(e) + sorted(o))
	else:
		return list(sorted(o) + sorted(e))

_l = [1,2,3,4,5,6,7,8,9]
print(sortFirst(_l, True))
print(sortFirst(_l, False))