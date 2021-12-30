def recursive(lst, item, left, right, cnt):
    if left > right:
        print("cnt = ", cnt)
        return -1
    else:
        mid = (left + right) // 2
        if lst[mid] == item:
            print("Cnt = ", cnt)
            return mid
        elif lst[mid] > item:
            return recursive(lst, item, left, mid, cnt+1)
        else:
            return recursive(lst, item, mid, right, cnt+1)

def withwhile(lst, item, left, right):
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            right = mid
        else:
            left = mid
    return -1

lst = [1,2,3,4,5,6,7,8,9,10]
item = 3

print(withwhile(lst, item, 0, len(lst)))
print(recursive(lst, item, 0, len(lst), 0))