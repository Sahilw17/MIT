nums=[1,99,101,98,2,5,3,100,1,1]
#l=4=[98,99,100,101]

n=len(nums)
# max_cnt=0
# for i in range(0,n):
#     num=nums[i]
#     cnt=1
#     while num+1 in nums:
#         cnt+=1
#         num=num+1
#     max_cnt=max(max_cnt,cnt)
# print(max_cnt)

#optimal
# nums.sort()
# count=0
# longest=0
# last_smaller=("-inf")
# for i in range(0,n):
#     num=nums[i]
#     if num-1==last_smaller:
#         count+=1
#         last_smaller=num
#     elif num-1 != last_smaller:
#         count=1
#         last_smaller=num
#     longest=max(longest,count)
# print(longest)


#most optimal
my_set=set()
for i in range(0,n):
    my_set.add(nums[i])

longest=0

for num in  my_set:
    if num-1 not in my_set:
        cnt=1
        x=num
        while x+1 in my_set:
            cnt+=1
            x+=1
        longest=max(longest,cnt)
print(longest)