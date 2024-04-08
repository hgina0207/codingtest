import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
graph=[]
dx=[0,-1,1,0]
dy=[-1,0,0,1]
fish=[[] for _ in range(7)]
init_x,init_y=0,0
for i in range(N):
    arr=list(map(int,input().split()))
    graph.append(arr)
    for j in range(len(arr)):
        if arr[j]==9:
            init_x=j
            init_y=i

shark_size=2
q=deque()
q.append((init_x,init_y))
graph[init_y][init_x]=0

def find_nearest_fish(x,y):
    visited=[[False]*N for _ in range(N)]
    queue=deque()
    queue.append((x,y,0))
    min_t=1e9
    near_fish_list=[]
    while queue:
        cur_x,cur_y,t=queue.popleft()
        if min_t<t+1: break
        for i in range(4):
            nx,ny=cur_x+dx[i],cur_y+dy[i]
            if 0>nx or nx>=N or ny<0 or ny>=N: continue
            if not visited[ny][nx]:
                if graph[ny][nx]!=0 and shark_size>graph[ny][nx]:
                    if len(near_fish_list)==0:
                        min_t=t+1
                    near_fish_list.append((ny,nx))
                    visited[ny][nx]=True
                elif graph[ny][nx]==0 or shark_size==graph[ny][nx]:
                    queue.append((nx,ny,t+1))
                    visited[ny][nx]=True
    if len(near_fish_list)>0:
        near_fish_list.sort(key=lambda x:(x[0],x[1]))
        graph[near_fish_list[0][0]][near_fish_list[0][1]]=0
        return near_fish_list[0][0],near_fish_list[0][1],min_t
    else: return -1,-1,-1
time=0
fish_num=0
while q:
    x,y=q.popleft()
    i,j,t=find_nearest_fish(x,y)
    if i<0: break
    else:
        q.append((j,i))
        time+=t
        fish_num+=1
        if fish_num==shark_size:
            fish_num=0
            shark_size+=1
    
print(time)