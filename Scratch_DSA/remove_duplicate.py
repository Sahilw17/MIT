#we have given the sorted array and our task is to bring all the unique elements at the starting of the list 
#and return the cnt of the  unique elements
# nums=[1,1,1,2,3,4,4,7,9,9,9,10]
# n=len(nums)
# freq_map={}
# for i in range (0,n):
#     freq_map[nums[i]]=0

# j=0
# for k in freq_map:
#     nums[j]=k
#     j+=1
# print(j)
# print(nums)

#TC=O(2N)
#Sc=O(N)

#Optimal solution

nums=[1,1,1,2,3,4,4,7,9,9,10]
n=len(nums)
i=0
j=i+1
if(n==1):
    print(1)
while j<n:
    if(nums[j]!=nums[i]):
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
print(i+1)
print(nums)