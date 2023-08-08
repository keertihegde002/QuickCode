from collections import defaultdict
def detect(adj,n):
    visited=[False]*n
    path_vis=[False]*n

    def dfs(node):
        visited[node]=True
        path_vis[node]=True
        for nei in adj[node]:
            if visited[nei]==False:
                if dfs(nei):
                    return True

            elif path_vis[nei]==True:
                    return True
        path_vis[node]=False
        return False

    for i in range(n):
        if visited[i]==False:
            if dfs(i)==True:
                return True
    return False

adj=defaultdict(list)
adj[0].append(1)
adj[0].append(2)
adj[1].append(2)
adj[2].append(0)
adj[2].append(3)
adj[3].append(3)
print(detect(adj,4))