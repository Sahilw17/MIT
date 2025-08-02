prices=[7,2,1,5,6,4,8]
# n=len(prices)
# maxp=0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if prices[j]>prices[i]:
#             p=prices[j]-prices[i]
#             maxp=max(maxp,p)
# print(maxp)

n=len(prices)
max_p=0
min_p=float("inf")
for i in range(0,n):
    min_p=min(min_p,prices[i])
    max_p=max(max_p,prices[i]-min_p)
print(max_p)