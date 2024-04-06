import sys
sys.setrecursionlimit(10**6)
n=int(input())
tree=[[] for _ in range(n+1)]

def dfs(start,dist):
    for s in tree[start]:
        e,c=s
        if distance[e]==-1:
            distance[e]=dist+c
            dfs(e,c+dist)
for _ in range(n-1):
    a,b,c=map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
if n==1:
    print(0)
else:

    distance=[-1]*(n+1)
    distance[1]=0
    dfs(1,0)
    start_idx=distance.index(max(distance))
    
    distance=[-1]*(n+1)
    distance[start_idx]=0
    dfs(start_idx,0)

    print(max(distance))