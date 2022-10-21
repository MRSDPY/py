import time


def prime(n):
    if n == 1:
        return False

    for i in range(2, n - 1):
        if n % i == 0:
            return False
    else:
        return True


count = 0
t1 = time.time()

number = int(input("Enter Number and our algorithm give this number'th prime : "))

for i in range(2, int(number*number)):
    ans = prime(i)
    if ans == True:
        count += 1

    if count == number:
        print(f"{count} -> {i} =", "IsPrime ->", ans)
        break

t2 = time.time()

print("Total Time :", t2 - t1)
