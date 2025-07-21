# nums=[3,9,5,6,7,2,10,9]
# n=len(nums)
# k=5
# k=n%k
# nums[:]=nums[n-k:] + nums[0:n-k]
# print(nums)

#MOst Optimal
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

nums=[3,9,5,6,7,2,10,9]
n=len(nums)
k=5
reverse(nums,k-n,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
print(nums)