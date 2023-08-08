from collections import defaultdict
def topoSort(adj,n):
    
    visited=set()
    stack=[]
    def dfs(node):
        visited.add(node)
        for nei in adj[node]:
            if nei not in visited:
                dfs(nei)

        stack.append(node)

    for i in range(n):
        print("enytere",i)
        if i not in visited:
            dfs(i)

    return stack[::-1]

adj=defaultdict(list)
adj[5].append(2)
adj[5].append(0)
adj[4].append(0)
adj[4].append(1)
adj[2].append(3)
adj[3].append(1)
print(topoSort(adj,6))


