x = int(input())
k = int(input())
if k == 0:
    i = str(x)[0]
    res = int(i * len(str(x)))
    if res < x:
        res = int(str(int(i) + 1) * len(str(x)))
    print(res)