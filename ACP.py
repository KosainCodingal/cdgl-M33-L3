a = [1, 5, 3, 67, 3, 5, 64, 23, 8, 2, 2]
s = a[0]
l = a[1]

for i in range(len(a)):
    if a[i] >= l: l = a[i]
    else:
        if s > a[i]: s = a[i]
        else: pass

sum = l - s
print(sum)
