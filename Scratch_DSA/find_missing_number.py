# nums=[9,6,4,2,3,5,7,0,1]
# n=len(nums)
# freq={}
# missing_num=0
# for i in range(0,n+1):
#     freq[i]=0
# for num in nums:
#     freq[num]+=1
# for k,v in freq.items():
#     if v==0:
#         missing_num=k
# print(missing_num)

nums=[1,0,3,4]
n=len(nums)

total=n*(n+1)/2
total_num=0
for num in nums:
    total_num+=num
total-=total_num
print(total)