def fictorial(n):
    if n == 0 :
        return 1
    else:
        return n * fictorial(n-1)


print(fictorial(5))