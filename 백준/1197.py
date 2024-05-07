import sys
import heapq
input=sys.stdin.readline
v,e=map(int,input().split())
visited=[False]*(v+1)
dic={}
for _ in range(e):
    a,b,c=map(int,input().split())
    if a in dic:
        dic[a].append((b,c))
    else:
        dic[a]=[(b,c)]
    if b in dic:
        dic[b].append((a,c))
    else:
        dic[b]=[(a,c)]

q=[]
visited[1]=True
for V,E in dic[1]:
    heapq.heappush(q,(E,V))

answer=0
while q:
    E,V=heapq.heappop(q)
    if not visited[V]:
        answer+=E
        visited[V]=True 
        for next_v,next_e in dic[V]:
            heapq.heappush(q,(next_e,next_v))
print(answer)