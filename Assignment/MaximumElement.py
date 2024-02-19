a=[6,7,11,4,2,21,67,0,24]

max=a[0]
n=len(a)
for i in range(1,n):
    if a[i]>max:
        max=a[i]
print("MAXIMUM ELEMENT: ",max)

