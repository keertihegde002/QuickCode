from collections import deque,defaultdict
def kahn(adj,n):
    indegree=[0]*n
    for i in range(n):
        if i in adj:
            for val in adj[i]:
                indegree[val]+=1
    q=deque()
    for i,e in enumerate(indegree):
        if e==0:
            q.append(i)
    topo=[]
    while q:
        curnode=q.popleft()
        topo.append(curnode)
        for nei in adj[curnode]:
            indegree[nei]-=1
            if indegree[nei]==0:
                q.append(nei)

    return topo

adj=defaultdict(list)
adj[5].append(2)
adj[5].append(0)
adj[4].append(0)
adj[4].append(1)
adj[2].append(3)
adj[3].append(1)
print(kahn(adj,6))
