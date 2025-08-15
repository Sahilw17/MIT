nums=[1,3,4,5,8,9,14,15,19,20,21]
target=2
def search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            low=mid
            high=mid-1
        else: 
            low=mid+1
    return low
print(search(nums,target))

#1231323213