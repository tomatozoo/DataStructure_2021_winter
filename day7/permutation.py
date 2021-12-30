def permutation(str, start, end):
    if start == end:
        return
    else:
        for i in range(start, end):
            str[start] = str[j]
            permutation()
    # for i in range(len):
    # i번째 원소로 시작하는 것 출력

permutation('STRING', 0, len('STRING'))