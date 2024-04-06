import sys
sys.setrecursionlimit(10**9)
INF=sys.maxsize
def dfs(s,e,d,dist,direc):
    if dist[e]>d:
        dist[e]=d

    for i in direc[e]:
        if i[0]!=s and i[0]!=x and visited[i[0]]==0 and d+i[1]<dist[i[0]] :
            visited[i[0]]=1
            dfs(e,i[0],d+i[1],dist,direc)
            visited[i[0]]=0

n,m,x=map(int,input().split())
visited=[0]*(n+1)
go=[[] for _ in range(n+1)]
back=[[] for _ in range(n+1)]
dist_go=[INF]*(n+1)
dist_back=[INF]*(n+1)
for i in range(m):
    s,e,t=map(int,input().split())
    go[e].append([s,t])
    back[s].append([e,t])
    if s==x:
        dist_back[e]=t
    if e==x:
        dist_go[s]=t
visited[x]=1
for i in go[x]:
    visited[i[0]]=1
    dfs(x,i[0],i[1],dist_go,go)
    visited[i[0]]=0

visited=[0]*(n+1)
visited[x]=1
for i in back[x]:
    visited[i[0]]=1
    dfs(x,i[0],i[1],dist_back,back)
    visited[i[0]]=0

max_dist=0
dist_back[x]=0
dist_go[x]=0
for i in range(1,n+1):
    if max_dist<dist_go[i]+dist_back[i]:
        max_dist=dist_go[i]+dist_back[i]
print(int(max_dist))