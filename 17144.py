import sys
from collections import deque
input=sys.stdin.readline

r,c,t=map(int,input().split())
board=[]
air=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(r):
    arr=list(map(int,input().split()))
    board.append(arr)
    if len(air)==0 and arr[0]==-1:
        air.append(i)
        air.append(i+1)

def plus_dust():
    after_dust=[[0]*c for _ in range(r)]
    after_dust[air[0]][0]=-1
    after_dust[air[1]][0]=-1
    
    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                dust=int(board[i][j]/5)
                for k in range(4):
                    nx=j+dx[k]
                    ny=i+dy[k]
                    if 0<=nx<c and 0<=ny<r and board[ny][nx]!=-1:
                        after_dust[ny][nx]+=dust
                        board[i][j]-=dust
                after_dust[i][j]=board[i][j]
    return after_dust
def operate_air():
    tmp_up=deque()
    tmp_up.append(board[air[0]][c-1])
    tmp_down=deque()
    tmp_down.append(board[air[1]][c-1])

    for i in range(c-1,1,-1):
        board[air[0]][i]=board[air[0]][i-1]
        board[air[1]][i]=board[air[1]][i-1]

    tmp_up.append(board[0][c-1])
    for i in range(air[0]):
        if i==air[0]-1:
            board[i][c-1]=tmp_up.popleft()
        else:
            board[i][c-1]=board[i+1][c-1]
    tmp_down.append(board[r-1][c-1])
    for i in range(r-1,air[1]):
        if i==air[1]+1:
            board[i][c-1]=tmp_down.popleft()
        else:
            board[i][c-1]=board[i-1][c-1]
    
    tmp_up.append(board[0][0])
    tmp_down.append(board[0][c-1])
    for i in range(c-1):
        if i==c-2:
            board[0][i]=tmp_up.popleft()
            board[r-1][i]=tmp_down.popleft()
        else:
            board[0][i]=board[0][i+1]
            board[r-1][i]=board[r-1][i+1]
            
    
    for i in range(air[0]-1,0,-1):
        if i==1:
            board[i][0]=tmp_up.popleft()
        else:
            board[i][0]=board[i-1][0]
            
    for i in range(air[1]+1,r-1):
        if i==r-2:
            board[i][0]=tmp_down.popleft()
        else:
            board[i][0]=board[i+1][0]
time=0
while time<=t:
    board=plus_dust()
    print("=============")
    for i in range(r):
        print(board[i])
    operate_air()
    time+=1
    print("oper")
    for i in range(r):
        print(board[i])

res=0
for i in range(r):
    for j in range(c):
        if board[i][j]!=-1:
            res+=board[i][j]

print(res)