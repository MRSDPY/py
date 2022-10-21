data2 = []

n = int(input("Enter number of elements : "))

data2 = [int(input(f"enter the index of {i}: ")) for i in range(n)]

search = int(input("Enter which element you want to search : "))


def binary(arr, l, h, value):
    if l <= h:
        mid = (l + h) // 2

        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            return binary(arr, mid + 1, h, value)
        elif value < arr[mid]:
            return binary(arr, l, mid - 1, value)
        else:
            pass
    else:
        return -1


result = binary(data2, 0, len(data2), search)
print("Element find on index :", result if result is not -1 else "No Data Found")
