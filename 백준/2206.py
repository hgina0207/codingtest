from collections import deque

N,M=map(int,input().split())
board=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
def bfs():
    queue=deque()
    queue.append((0,0,0))
    while queue:
        x,y,b=queue.popleft()
        if x==M-1 and y==N-1:
            return visited[y][x][b]
        for i in range(4):
            cx,cy=x+dx[i],y+dy[i]
            if (cx<M and cx>=0) and (cy<N and cy>=0):
                if board[cy][cx]==0 and visited[cy][cx][b]==0:
                    visited[cy][cx][b]=visited[y][x][b]+1
                    queue.append((cx,cy,b))
                elif b==0 and board[cy][cx]==1:
                    visited[cy][cx][1]=visited[y][x][b]+1
                    queue.append((cx,cy,1))

    return -1
for i in range(N):
    board.append(list(map(int,list(input()))))
visited[0][0][0]=1
print(bfs())
