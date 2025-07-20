num=[3,5,6,4,8,9,10,7,1]
n=len(num)
for i in range(1,n):
    key=num[i]
    j=i-1
    while j>=0 and num[j]>key:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key
print(num)

#tc: O(n^2)
#sc: O(1)