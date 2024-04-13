import sys
import copy
input=sys.stdin.readline

def dfs(count,x,y,go_start,visited_tmp):
    global res
    visited_tmp1=copy.deepcopy(visited_tmp)
    if go_sadari(go_start,visited_tmp1):
        res=min(count,res)
        return
    if count==3 or res<=count:
        return
    
    for i in range(x,h):
        if i!=x: y=1
        for j in range(y,n-1):
            if sadari[i][j]==0 and sadari[i][j+1]==0 and sadari[i][j-1]==0:
                sadari[i][j]=1
                for k in range(1,n+1):
                    if [i,j] in visited[k] or [i,j+1] in visited[k]:
                       dfs(count+1,i,j+2,k)
                       break
                    else: dfs(count+1,i,j+2,1)
                sadari[i][j]=0




def go_sadari(go_start,visited_tmp):
    for j in range(go_start,n+1):
        now=j
        for i in range(1,h+1):
            if sadari[i][now]==1:
                now+=1
            elif sadari[i][now-1]==1:
                now-=1
        if j!=now:
            return False
            
    return True
n,m,h=map(int,input().split())
sadari=[[0]*(n) for i in range(h)]
visited=[[[False]*n for i in range(h)] for _ in range(n)]
line=[]
for i in range(m):
    a,b=map(int,input().split())
    sadari[a-1][b-1]=1

if m==0:
    print(0)
else:
    res=4
    dfs(0,0,0)
    if res==4: print(-1)
    else: print(res)
