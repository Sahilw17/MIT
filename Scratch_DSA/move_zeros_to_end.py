#brute sln
# nums=[1,2,0,4,3,0,0,0,3,5,1]
# temp=[]
# n=len(nums)

# for i in range(0,n):
#     if(nums[i]!=0):
#         temp.append(nums[i])

# n2=len(temp)
# for i in range(0,n2):
#     nums[i]=temp[i]

# for i in range(n2,n):
#     nums[i]=0

# print(nums)


#Optimal Solution
nums=[1,0,2,4,3,0,0,3,5,1]
def move_zero(nums):
    n=len(nums)
    i=0
    if(n==1):
        return
    while i<n:
        if nums[i]==0:
            break
        i+=1
        if i==n:
            return
        j=i+1
        while j<n:
            if(nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1

move_zero(nums)
print(nums)


