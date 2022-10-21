cach_memory = {}


def fibonacci(n):
    assert type(n) == int, "Please Enter number in integer"

    assert n >= 1, "Please Enter number greater than 1 or equal to 1"

    if n in cach_memory:
        return cach_memory[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    cach_memory[n] = value

    return value


n = 9999

for i in range(1, n):
    print(f"{i} =", fibonacci(i))
