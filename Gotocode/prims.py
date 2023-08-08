import heapq
def pMST(adj):
    sum=0
    pq=[]
    visited=set()
    heapq.heappush(pq,(0,0))
    while pq:
        weight,node=heapq.heappop(pq)
        if node in visited:
            continue
        sum+=weight
        visited.add(node)
        for nei,neiw in adj[node]:
            if nei not in visited:
                heapq.heappush(pq,(neiw,nei))

    return sum

adj={0:[(1,8),(2,4)],1:[(0,8),(3,1)],2:[(0,4),(3,7)],3:[(1,1),(2,7)]}
print(pMST(adj))