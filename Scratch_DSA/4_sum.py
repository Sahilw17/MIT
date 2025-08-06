# nums=[1,0,-1,0,-2,2]
# n=len(nums)
# mset=set()
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
# result=set()
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             fourth=-(nums[i]+nums[j]+nums[k])
#             mset.add(k)
#             if fourth in mset:
#                 temp=[nums[i],nums[j],nums[k],fourth]
#                 temp.sort()
#                 result.add(tuple(temp))
# print(result)



#optimal 

nums=[1,1,1,1,2,2,3,3,3,4,4,4,5,5]
n=len(nums)
target=8
ans=[]
nums.sort()
for i in range(0,n):
    if i>0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and nums[i]==nums[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            total=nums[i]+nums[j]+nums[k]+nums[l]
            if total==target:
                ans.append([nums[i],nums[j],nums[k],nums[l]])
                k+=1
                l-=1
                while k<l and nums[k]==nums[k-1]:
                    k+=1
                while l>k and nums[l]==nums[l-1]:
                    l-=1
            
            elif total<target:
                k+=1
            
            else:
                l-=1
print(ans)