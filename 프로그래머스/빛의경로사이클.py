import sys
sys.setrecursionlimit(10**6)
def solution(grid):
    answer=[]
    visited=[[[False]*len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    
    
    def dfs(y,x,direc,cnt):
        visited[direc][y][x]=True
        if grid[y][x]=='L':
            if direc==0: direc=2
            elif direc==1: direc=3
            elif direc==2: direc=1
            else: direc=0
        elif grid[y][x]=='R':
            if direc==0: direc=3
            elif direc==1: direc=2
            elif direc==2: direc=0
            else: direc=1
            
        ny=(y+dy[direc])%len(grid)
        nx=(x+dx[direc])%len(grid[0])
        if visited[direc][ny][nx]:
            answer.append(cnt+1)
            return
        else: dfs(ny,nx,direc,cnt+1)
        
    for d in range(4):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[d][i][j]:
                    dfs(i,j,d,0)
    
    
    return sorted(answer)