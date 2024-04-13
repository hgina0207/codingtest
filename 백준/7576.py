import sys
from collections import deque
input=sys.stdin.readline
m,n=map(int,input().split())
tomato=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
ripe=deque()

def bfs():
    date=1
    while ripe:
        y,x=ripe.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n and tomato[ny][nx]==0:
                ripe.append((ny,nx))
                tomato[ny][nx]=tomato[y][x]+1
                date=tomato[y][x]+1
    
    for tom in tomato:
        if 0 in tom: 
            return -1

    return date-1

for i in range(n):
    tom=list(map(int,input().split()))
    for j in range(m):
        if tom[j]==1:
            ripe.append((i,j))
    tomato.append(tom)
if len(ripe)==0:
    print(-1)
else:
    print(bfs())

