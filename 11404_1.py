import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[1e9]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=min(graph[a][b],c)

for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            graph[start][end]=min(graph[start][end],graph[start][mid]+graph[mid][end])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=' ')
    print()