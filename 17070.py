import sys
input=sys.stdin.readline
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

cnt=0
def dfs(x,y,status):
    global cnt
    if x==N-1 and y==N-1:
        cnt+=1
        return
    if status==1 or status==3:
        if x+1<N and graph[y][x+1]==0:
            dfs(x+1,y,1)
    if status==2 or status==3:
        if y+1<N and graph[y+1][x]==0:
            dfs(x,y+1,2)
    if x+1<N and y+1<N:
        if graph[y][x+1]==0 and graph[y+1][x]==0 and graph[y+1][x+1]==0:
            dfs(x+1,y+1,3)
dfs(1,0,1)
print(cnt)