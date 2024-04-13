import sys
input=sys.stdin.readline

n,m,r=map(int,input().split())
items=[0]+list(map(int,input().split()))
graph=[[int(1e9)]*(n+1) for _ in range(n+1)]
for i in range(r):
    a,b,l=map(int,input().split())
    graph[a][b]=min(l,graph[a][b])
    graph[b][a]=min(l,graph[b][a])

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][k]+graph[k][b],graph[a][b])

dp=[0]*(n+1)
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]<=m:
            dp[a]+=items[b]

print(max(dp))