import sys,copy
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
home=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            home.append((i,j))
        elif graph[i][j]==2:
            chicken.append((i,j))

distance=[[0]*len(home) for _ in range(len(chicken))]

for i in range(len(chicken)):
    for j in range(len(home)):
        distance[i][j]=abs(home[j][0]-chicken[i][0])+abs(home[j][1]-chicken[i][1])

def solve(idx,cnt,arr,min_dist):
    if cnt==m:
        if min_dist>sum(arr):
            min_dist=sum(arr)
    else:
        if cnt==0:
            for i in range(0,len(chicken)):
                arr=copy.deepcopy(distance[i])                
                min_dist=solve(i,cnt+1,arr,min_dist)
        else:
            for i in range(idx+1,len(chicken)):                
                tmp=copy.deepcopy(arr)
                for j in range(len(home)):
                    tmp[j]=min(tmp[j],distance[i][j])
                min_dist=solve(i,cnt+1,tmp,min_dist)
    return min_dist

print(solve(0,0,[],int(1e9)))