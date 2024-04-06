from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
graph=[[] for _ in range(N+1)]

q=deque()
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q.append(1)
res=[0]*(N+1)
visited=[False]*(N+1)
visited[1]=True
while q:
    a=q.pop()
    for i in graph[a]:
        if not visited[i]:
            q.append(i)
            res[i]=a
            visited[i]=True
for i in range(2,N+1): print(res[i])