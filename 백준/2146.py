import sys
from collections import deque
import heapq
n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

nation_num=0
visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]==1 and not visited[i][j]:
            nation_num+=1
            visited[i][j]=True
            board[i][j]=nation_num
            q=deque()
            q.append((i,j))
            while q:
                y,x=q.popleft()
                for k in range(4):
                    ny=y+dy[k]
                    nx=x+dx[k]
                    if 0<=nx<n and 0<=ny<n:
                        if board[ny][nx]==1 and not visited[ny][nx]:
                            board[ny][nx]=nation_num
                            q.append((ny,nx))
                            visited[ny][nx]=True

def make_bridge(nation):
    dist=[[-1]*n for _ in range(n)]
    sea=deque()
    for i in range(n):
        for j in range(n):
            if board[i][j]==nation:
                dist[i][j]=0
                sea.append((i,j))
    while sea:
        y,x=sea.popleft()
        for k in range(4):
            ny=y+dy[k]
            nx=x+dx[k]
            if 0<=nx<n and 0<=ny<n:
                if board[ny][nx]!=0 and board[ny][nx]!=nation:
                    return dist[y][x]
                elif board[ny][nx]==0 and dist[ny][nx]==-1:
                    dist[ny][nx]=dist[y][x]+1
                    sea.append((ny,nx))
    return 1e9

answer=1e9
for i in range(1,nation_num+1):
    answer=min(answer,make_bridge(i))

print(answer)