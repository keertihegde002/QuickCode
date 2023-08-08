from collections import deque,defaultdict 
def bipartatie(adj):
    
    n=len(adj) # take v 
    visited=[-1]*n
    def solve(node):
        visited[node]=0
        q=deque()
        q.append(node)
        while q:
            curnode=q.pop()
            curcolor=visited[curnode]
            for nei in adj[curnode]:
                if visited[nei]!=-1:
                    if visited[nei]==curcolor:
                        return False
                else:
                    visited[nei]=0 if curcolor==1 else 1
                    q.append(nei)
        return True

    for i in range(n):
        if visited[i]==-1:
            if not solve(i):
                return False
    return True

adj=defaultdict(list)
adj[0].append(1)
adj[1].extend([0,2,3])
adj[2].extend([1,4])
adj[3].extend([1,5])
adj[5].extend([3,6])
adj[4].extend([2,6])
adj[6].extend([4,5,7])
adj[7].append(6)
print(bipartatie(adj))
