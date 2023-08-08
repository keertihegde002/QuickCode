import heapq
def dijkstra(source):
    dist=[float('inf') for i in range(v)]
    pq=[]
    heapq.heappush(pq,(0,source))
    dist[source]=0
    while pq:
        curdist,curnode=heapq.heappop(pq)

        for neinode,neidist in adj[curnode]:
            if neidist+curdist<dist[neinode]:
                dist[neinode]=neidist+curdist
                heapq.heappush(pq,(dist[neinode],neinode))

    return dist
