import sys
import heapq
input=sys.stdin.readline

n,e=map(int,input().split())
graph=[[] for _ in range(n)]

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

v1,v2=map(int,input().split())


def dijkstra(start):
    distance=[1e9]*n
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

    return distance

start_dist=dijkstra(0)
v1_dist=dijkstra(v1-1)
v2_dist=dijkstra(v2-1)

v1_path=start_dist[v1-1]+v1_dist[v2-1]+v2_dist[n-1]
v2_path=start_dist[v2-1]+v2_dist[v1-1]+v1_dist[n-1]

res=min(v1_path,v2_path)

print(res if res<1e9 else -1)