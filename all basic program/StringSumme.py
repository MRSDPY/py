def summarizeString(s):
	letter = []
	ULetter = []
	LLetter = []

	digit = []
	oddDigit = []
	evenDigit = []

	for i in s:
		if i.isdigit():
			digit.append(int(i))
			if int(i) % 2 == 0:
				evenDigit.append(i)
			else:
				oddDigit.append(i)

		if i.isupper():
			ULetter.append(i)
			letter.append(i)

		if i.islower():
			LLetter.append(i)
			letter.append(i)

	print("Letters In String: ", letter)
	print("Sorted Letter: ", sorted(letter))
	print("Upper Case : ", ULetter)
	print("Lowercase: ", LLetter)
	print("Numbers : ", digit)
	print("Sorted Number: ", sorted(digit))
	print("Sum : ", sum(digit))
	print("Even : ", evenDigit)
	print("Odd: ", oddDigit)

summarizeString("aaddddd23445566DDFRRgyt5")