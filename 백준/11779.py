import sys, heapq
input=sys.stdin.readline
n=int(input())
m=int(input())
bus=[[] for _ in range(n+1)]
for i in range(m):
    s,e,c=map(int,input().split())
    bus[s].append((e,c))

start,end=map(int,input().split())

distance=[int(1e9)]*(n+1)
nearest=[start]*(n+1)
def dijkstra():
    q=[(0,start)]
    while q:
        dist,now=heapq.heappop(q)
        if dist>distance[now]:
            continue

        for next_node,next_dist in bus[now]:
            cost=dist+next_dist
            if cost<distance[next_node]:
                nearest[next_node]=now
                distance[next_node]=cost
                heapq.heappush(q,(cost,next_node))
dijkstra()
print(distance[end])

res=[]
node=end
while node!=start:
    res.append(node)
    node=nearest[node]

res.append(start)

print(len(res))
for i in range(len(res)-1,-1,-1):
    print(res[i],end=' ')