list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list(map(int, input().split()))
sum1 = max(sum(list2), sum(list1))
b = max(list1[0], list2[0])
c = max(list1[1], list2[1])
d = max(list1[2], list2[2])

a = sum1 - list3[0] - list3[1]
if a < 0:
    print(0)
elif a > b:
    print(a)
elif sum(list1) < sum1:
    if a > list2[0]:
        print(a)
    elif a == list2[0]:
        if list3[0] > list2[1]:
            print(a)
        elif list3[0] < list2[1]:
            print(a + 1)
        elif list3[0] == list2[1]:
            print(a + 1)
    else:
        print(a + 1)

elif sum(list2) < sum1:
    if a > list1[0]:
        print(a)
    elif a == list1[0]:
        if list3[0] > list1[1]:
            print(a)
        elif list3[0] < list1[1]:
            print(a + 1)
        elif list3[0] == list1[1]:
            print(a + 1)
    else:
        print(a + 1)
else:
    print(a + 1)
