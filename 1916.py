import heapq
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())

bus=[[] for _ in range(n+1)]
cost=[1e9]*(n+1)
def dijkstra(start,end):
    heap=[]
    cost[start]=0
    heapq.heappush(heap,[0,start])

    while heap:
        c,v=heapq.heappop(heap)
        if cost[v]<c:
            continue
        for next_v,next_cost in bus[v]:
            if c+next_cost<cost[next_v]:
                cost[next_v]=c+next_cost
                heapq.heappush(heap,[c+next_cost,next_v])
    return cost[end]
        
for i in range(m):
    a,b,c=map(int,input().split())
    bus[a].append((b,c))

start,end=map(int,input().split())
print(dijkstra(start,end))