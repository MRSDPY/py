def pattern(s):
	# a* / a*b+ / abb => None / aaaaaaaaa / aaaaaabbbb/ aaaaaaab / abb / bbbbbb / b

	state = 0

	if len(s) == 0:
		return "Pattern matched under 'a*' rule."

	if s == "abb":
		return "Pattern matched under 'abb' rule."

	for i in s:
		if state == 0:
			if i == "a":
				state = 1
			elif i == "b":
				state = 2
			else:
				state = 5
		elif state == 1:
			if i == "a":
				state = 1
			elif i == "b":
				state = 2
			else:
				state = 5
		elif state == 2:
			if i == "a":
				state = 5
			elif i == "b":
				state = 2
			else:
				state = 5
		elif state == 5:
			return "Pattern not matched."

	if state == 1:
		return "Pattern matched under 'a*' rule."
	elif state == 2:
		return "Pattern matched under 'a*b+' rule."


print(pattern(input("Enter Pattern : ")))
