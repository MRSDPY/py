c = input("Enter Comment : ")

if c.startswith("//"):
	print("Single Line Comment.")
elif c.startswith("/*") and c.endswith("*/"):
	print("Multi Line Comment.")
else:
	print("This is not a comment.")
