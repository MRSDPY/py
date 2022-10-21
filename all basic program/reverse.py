li = [1, 3, 4, 2]
t = 5
ans = []
ar = []

for a in li:
    ar.append(int(a))

for a in range(len(ar)):
    for b in range(a+1,len(ar)):
        sum = ar[a] + ar[b]
        if sum == t:
           ans = [a , b]
           print(ans)
        else:
            print("error")



