def function(bu, x, y):
    if bu == 'r':
        y += 1
        return (x, y)
    elif bu == 'l':
        y -= 1
        return (x, y)
    elif bu == 'u':
        x -= 1
        return (x, y)
    elif bu == 'd':
        x += 1
        return (x, y)


n, m = list(map(int, input().split()))
li = []
for i in range(n):
    li.append(list(input()))
x, y = list(map(int, input().split()))
li2 = []
while True:
    try:
        if (x, y) in li2:
            print('NO')
            break
        li2.append((x, y))
        ui = li[x-1][y - 1]
        function(li[x - 1][y - 1], x, y)
        print(li2)
    except:
        print('YES')
        break

