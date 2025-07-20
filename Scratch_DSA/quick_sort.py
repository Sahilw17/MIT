nums=[4,1,7,6,3,2,8]
def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<high+1:
            i+=1
        while nums[j]>=pivot and j>=low+1:
            j-=1
        if(i<j):
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick(nums,low,high):
    if low<high:
        p=partition(nums,low,high)
        quick(nums,low,p-1)
        quick(nums,p+1,high)

(quick(nums,0,len(nums)-1))
print(nums)    