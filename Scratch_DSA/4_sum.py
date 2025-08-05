nums=[1,0,-1,0,-2,2]
n=len(nums)
mset=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             for l in range(k+1,n):
#                 if(nums[i]+nums[j]+nums[k]+nums[l]==0):
#                     temp=[nums[i],nums[j],nums[k],nums[l]]
#                     temp.sort()
#                     mset.add(tuple(temp))
# print(mset)

#better sln
result=set()
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            fourth=-(nums[i]+nums[j]+nums[k])
            mset.add(k)
            if fourth in mset:
                temp=[nums[i],nums[j],nums[k],fourth]
                temp.sort()
                result.add(tuple(temp))
print(result)
