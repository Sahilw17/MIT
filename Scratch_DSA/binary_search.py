nums=[2,4,6,7,8,11,18,19]
target=11
def binary(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid+1 
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(binary(nums,target))