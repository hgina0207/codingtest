import sys
import copy
input=sys.stdin.readline

def dfs(depth,kan_tmp,ms):
    global min_size
    if depth==len(cctv):
        min_size=min(min_size,ms)
        return
    kan_tmp1=copy.deepcopy(kan_tmp)
    cctv_i=cctv[depth][0]
    cctv_j=cctv[depth][1]
    ms_tmp=ms
    if kan_tmp[cctv_i][cctv_j]==1:
        for i in range(4):
            ms_tmp=go_back_cctv(i,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
            dfs(depth+1,kan_tmp1,ms_tmp)
            kan_tmp1=copy.deepcopy(kan_tmp)
            ms_tmp=ms

    elif kan_tmp[cctv_i][cctv_j]==2:
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#0,1
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)
        kan_tmp1=copy.deepcopy(kan_tmp)
        ms_tmp=ms
        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#2,3
        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)
    
    elif kan_tmp[cctv_i][cctv_j]==3:
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#0,3
        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)

        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)#0,2
        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)

        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#1,2
        dfs(depth+1,kan_tmp1,ms_tmp)

        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)
        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#1,3
        dfs(depth+1,kan_tmp1,ms_tmp)
        
    elif kan[cctv_i][cctv_j]==4:
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)#0,1,2
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)#1,2,3
        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)#0,2,3
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)
        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,1,ms_tmp)#0,1,3
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)

    elif kan[cctv_i][cctv_j]==5:
        ms_tmp=go_back_cctv(0,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        ms_tmp=go_back_cctv(1,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        ms_tmp=go_back_cctv(2,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        ms_tmp=go_back_cctv(3,cctv_i,cctv_j,kan_tmp1,-1,ms_tmp)
        dfs(depth+1,kan_tmp1,ms_tmp)


def go_back_cctv(i,cctv_i,cctv_j,kan_tmp1,go_back,ms):
    nx=cctv_j+dx[i]
    ny=cctv_i+dy[i]
    while (0<=nx<m) and (0<=ny<n):
        if kan_tmp1[ny][nx]==6: break
        elif 1<=kan_tmp1[ny][nx]<=5: 
            nx+=dx[i]
            ny+=dy[i]
            continue
        else: 
            if kan_tmp1[ny][nx]==0 and go_back==-1: ms-=1
            elif kan_tmp1[ny][nx]==-1 and go_back==1: ms+=1
            kan_tmp1[ny][nx]+=go_back
        nx+=dx[i]
        ny+=dy[i]
    return ms
n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
kan=[]
cctv=[]
min_size=1e9
wall_size=n*m
for i in range(n):
    kan.append(list(map(int,input().split())))
    for j in range(m):
        if 1<=kan[i][j]<6:
            cctv.append([i,j])
        elif kan[i][j]==6:
            wall_size-=1
dfs(0,kan,wall_size-len(cctv))
print(min_size)