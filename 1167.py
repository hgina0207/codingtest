import sys
sys.setrecursionlimit(10**9)
def dfs(v1,n):
    for j in tree[v1]:
        if visited[j[0]]==-1:
            visited[j[0]]=n+j[1]
            dfs(j[0],n+j[1])

v=int(input())
tree=[[] for i in range(v+1)]
for i in range(v):
    tree_v=list(map(int,input().split()))[:-1]
    for j in range(1, len(tree_v)//2 + 1):
        tree[tree_v[0]].append([tree_v[j*2 - 1],tree_v[j*2]])
visited=[-1]*(v+1)
visited[1]=0
dfs(1,0)
max_v=visited.index(max(visited))
visited=[-1]*(v+1)
visited[max_v]=0
dfs(max_v,0)
print(max(visited))