def swap(str, a, b):
    str[a], str[b]
    return str
    
def permutation(level, str):
    str = (list(str))
    if level >= len(str):
        print("".join(str))
        return
    
    else:
        for i in range(level, len(str)):
            str[level], str[i] = str[i], str[level]
            permutation(level+1, str)
    return

permutation(0,'STRI')