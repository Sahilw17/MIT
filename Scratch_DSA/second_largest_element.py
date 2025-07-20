#brute solution
# nums=[55,32,97,-55,45,32,88,21]
# n=len(nums)
# lar=float("-inf")
# seclar=float("-inf")
# for i in range(0,n):
#     if(nums[i]>lar):
#         lar=nums[i]

# for i in range(0,n):
#     if(nums[i]<lar and nums[i]>seclar):
#         seclar=nums[i]
# print(seclar)

nums=[55,32,97,-55,45,32,88,21]
n=len(nums)
lar=float("-inf")
slar=float("-inf")
for i in range(0,n):
    if(nums[i]>lar):
        slar=lar
        lar=nums[i]
    elif(nums[i]>slar and nums[i]!=lar):
        slar=nums[i]
print(slar)

#TC:O(N)
#SC:O(1)