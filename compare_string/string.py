string = "shubham is join gtm"

string2 = "shubham is join google ans microsoft"

a = list(string.split(" "))

b = list(string2.split(" "))

ans = []
le = 0
f1 = 0
f2 = 0


while f1 < len(b) or f2 < len(a):
        if a[f2] == b[f1]:
            f1 = f1+1
            f2 = f2+1
            continue
        else:
            ans.append(a[f2])
            ans.append(b[f1])
f1 = f1+1
f2 = f2+1
print(f1, "  ", f2)


print(ans)
