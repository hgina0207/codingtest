import sys
import copy
from itertools import combinations

def bfs():
    for wall_combi in combinations(empty_loc,3):
        b=copy.deepcopy(board)
        for wall in wall_combi:
            b[wall[0]][wall[1]]=1

        queue=copy.deepcopy(virus_loc)
        
        while queue:
            v=queue.pop(0)
            for i in range(4):
                nx=v[0]+dx[i]
                ny=v[1]+dy[i]
                if nx>=0 and nx<n and ny>=0 and ny<m and b[nx][ny]==0:
                    b[nx][ny]=2
                    queue.append([nx,ny])
        
        global res
        count=0
        for i in range(n):
            for j in range(m):
                if b[i][j]==0:
                    count+=1
        
        if res<count: res=count

        
n,m=map(int,sys.stdin.readline().split())
board=[]
virus_loc=[]
empty_loc=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
res=0
for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    for j in range(len(line)):
        if line[j]==2: virus_loc.append([i,j])
        elif line[j]==0: empty_loc.append([i,j])
    board.append(line)

bfs()
print(res)