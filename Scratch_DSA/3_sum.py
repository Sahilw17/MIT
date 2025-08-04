harr=[-1,0,1,2,-1,-4,0]
mset=set()

n=len(harr)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if((harr[i]+harr[j]+harr[k])==0):
                temp=[harr[i],harr[j],harr[k]]
                temp.sort()
                mset.add(tuple(temp))
print( mset)