def identifier(s):

	if s[0].isalpha() and s[0] == "_":
		return True

	for i in s[1:]:
		if not i.isalnum() and i != "_":
			return False

	return True


if identifier(input("Enter String : ")):
	print("Valid Identifier")
else:
	print("Not Valid Identifier")