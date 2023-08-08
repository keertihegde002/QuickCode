def subsets(nums):
    n=len(nums)
    res=[]
    for i in range(0,(1<<n)):
        cur=[]

        for j in range(n):

            if ((1<<j)&i):
                cur.append(nums[j])
        res.append(cur)

    return res

print(subsets([1,2,3]))