str = input("Enter String : ")
pattern = input("Enter Pattern : ")

i = 0
s_index = 0
j = -1
p_index = len(pattern)

while (len(str) - i) >= len(pattern):
    s_index = i
    while str[s_index] == pattern[j + 1]:
        s_index += 1
        j += 1
        p_index -= 1
        if p_index <= 0:
            print("pattern match")
            exit()

    i += 1
    s_index = 0
    j = -1
    p_index = len(pattern)
else:
    print("pattern not match")
