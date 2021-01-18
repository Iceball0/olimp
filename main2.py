x = int(input())
k = int(input())


def check(lister):
    lister = list(map(int, list(str(lister))))
    c = max(lister)
    d = min(lister)
    b = lister.count(c)
    d = lister.count(d)
    if b == len(lister) - 1 and d == 1:
        return True
    elif b == 1 and d == len(lister) - 1:
        return True
    return False


if k == 0:
    elem = str(x)[0]
    total = int(elem * len(str(x)))
    if total < x:
        total = int(str(int(elem) + 1) * len(str(x)))
    print(total)
if k == 1:
    lst = list(map(int, list(str(x))))
    if len(str(x)) > 1:
        for i in range(x + 10 ** 17):
            if check(x + i):
                print(x + i)
                break
    else:
        print(x)
