def seqsearch(num, item, n):
    for i in range(n):
        if item == num[i]:
            return i
    return -1

def binary_search(lst, item, left, right):
    while left <= right:
        mid = (left + right) // 2
        if item == lst[mid]: 
            return mid
        else:
            if item == lst[mid]:
                return mid
            else: 
                left = mid + 1
                
    return -1

mylist = [5,8,91,111]
for item in [60,9,10]:
    pos = binary_search(mylist, item, 0, len(mylist)-1)
    print("position of %2d = %2d" % (item, pos))
    
def interpolate_search(num, key, left, right):
    while left <= right:
        if key < num[left] or key > num[right]:
            break
        pos = left + (key - num[left]) * (right-left)// (num[right]-num[left])
        if key > num[pos]:
            left = pos + 1
        elif key < num[pos]:
            right = pos - 1
        else:
            return pos
    return -1

lst = [2,3,5,7,8,10,13,20,25,39,45,55]
for key in [39,2,55,60,1]:
    pos = interpolate_search(lst, key, 0, len(lst)-1)
    print("%2d is in %2d" % (key, pos))