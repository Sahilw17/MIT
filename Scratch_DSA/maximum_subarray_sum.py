nums=[-2,1,-3,4,-1,2,1,-5,4]
#output willl be the sum of maximum subarray 4 + -1 + 2 + 1= 6
n=len(nums)
# maxi=float("-inf")
# for i in range(0,n):
#     total=0
#     for j in range(i,n):
#         total=total+nums[j]
#         maxi=max(maxi,total)
# print(maxi)

#optimal sln

maxi=float("-inf")
total=0
for i in range(0,n):
    total+=nums[i]
    maxi=max(maxi,total)
    if(total<0):
        total=0
print(maxi)
