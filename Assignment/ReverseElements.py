a=[6,7,11,4,2,21,67,0,24]

#1st Method
print(a[::-1])

 #2nd METHOD
n=len(a)
for i in range((int)(n/2)):
    a[i],a[n-1-i]=a[n-1-i],a[i]
print(a)