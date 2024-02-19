a = [-6, -4, -9, -12, -2]
max = a[0]
n = len(a)
for i in range(1, n):
    if a[i] > max:
        max = a[i]

print("Maximum Negative Element in an array:",max)