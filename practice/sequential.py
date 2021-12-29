def sequential(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return -1

print(sequential([1,23,4,5],1))