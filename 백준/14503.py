import sys
input=sys.stdin.readline


def dfs(r,c,d,count):
    if board[r][c]==0:
        board[r][c]=2
        count+=1
    dirty_space=0
    for i in range(1,5):
        nx=c+dx[(d-i)%4]
        ny=r+dy[(d-i)%4]
        nd=(d-i)%4
        if (0<=nx<m) and (0<=ny<n) and board[ny][nx]==0:
            dfs(ny,nx,nd,count)
            dirty_space+=1
            break
    
    if dirty_space==0: 
        nx=c+dx[(d+2)%4]
        ny=r+dy[(d+2)%4]
        if not ((0<=nx<m) and (0<=ny<n)) or board[ny][nx]==1:
            print(count)
            return
        else: dfs(ny,nx,d,count)
n,m=map(int,input().split())
row,col,direc=map(int,input().split())

board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[-1,0,1,0]


dfs(row,col,direc,0)