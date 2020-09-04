count = int(input())
i = 0
a = list()
while i < count:
    a.append(int(input()))
    i = i+1
a.sort()
i = 0
while i< count:
    if a[i]>0 or a[i] == 0:
        print(a[i])
    i = i+1
i = 0
while i< count:
    a[i] = a[i] * (-1)
    i = i + 1
a.sort()
i = 0
while i< count:
    if a[i]>0:
        print(a[i]*-1)
    i = i+1
i = 0
