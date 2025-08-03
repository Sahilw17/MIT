nums=[5,10,-3,-1,-10,6]
#// new_num=[5,-3,10,-1,6,-10]
# pos=[]
# neg=[]
# num=[]
# n=len(nums)
# for i in nums:
#     if(i>0):
#         pos.append(i)
#     else:
#         neg.append(i)
# for i in range(0,len(pos)):
#     num.append(pos[i])
#     num.append(neg[i])
# print(num)

#Optimal solution

n=len(nums)
reuslt=[0]*6
posind,negind=0,1
for i in range(0,n):
    if nums[i]>=0:
        reuslt[i]=nums[posind]
        posind+=2
    else:
        reuslt[i]=nums[negind]
        negind+=2
print(reuslt)