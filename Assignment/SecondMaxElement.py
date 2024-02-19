a=[7,3,2,11,21,63,3,8]

max=a[0]
second_max=a[0]
n=len(a)
for i in range(1,n):
    if a[i]>max:
        second_max=max
        max=a[i]
    elif a[i]>second_max:
        second_max=a[i]
 
print("Second Maximum Element:",second_max)