def binary(lst, item, left, right):
    while True:
        if left > right:
            break
        mid = (left + right) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1

lst = [1,2,3,34,55,67,89,100]
print(binary(lst, 100, 0, len(lst)-1))