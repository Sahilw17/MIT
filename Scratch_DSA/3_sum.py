# harr=[-1,0,1,2,-1,-4,0]
# mset=set()

# n=len(harr)
# for i in range(0,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if((harr[i]+harr[j]+harr[k])==0):
#                 temp=[harr[i],harr[j],harr[k]]
#                 temp.sort()
#                 mset.add(tuple(temp))
# print( mset)

nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
n=len(nums)
ans=[]
nums.sort()
for i in range(0,n):
    if i!=0 and nums[i]==nums[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        sum=nums[i]+nums[j]+nums[k]
        if(sum<0):
            j+=1
        elif(sum>0):
            k-=1
        else:
            temp=[nums[i],nums[j],nums[k]]
            ans.append(temp)
            j+=1
            k-=1
        
        while j<k and nums[j]==nums[j-1]:
            j+=1
        
        while j<k and nums[k]==nums[k-1]:
            k-=1
print(ans)