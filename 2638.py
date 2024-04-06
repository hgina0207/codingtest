import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def is_out_air():
    visited=[[False]*m for _ in range(n)]
    flag=False
    q=deque()
    q.append((0,0))
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny<0 or ny>=n or nx<0 or nx>=m: continue
            elif graph[ny][nx]<=0 and not visited[ny][nx]:
                q.append((ny,nx))
                graph[ny][nx]-=1
                visited[ny][nx]=True
            elif graph[ny][nx]==1: flag=True
    return flag

def count_air(y,x):
    cnt=0
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ny<0 or ny>=n or nx<0 or nx>m: continue
        elif graph[ny][nx]<0:
            cnt+=1
    return cnt
time=0
while is_out_air():
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1 and count_air(i,j)>1:
                graph[i][j]-=1
    
    time+=1
print(time)
