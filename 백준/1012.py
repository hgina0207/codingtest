import sys
sys.setrecursionlimit(10**9)
t=int(input())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
c=0

def dfs(x,y):
    visitied[x][y]=1
    for i in range(4):
            curr_x,curr_y=x+dx[i],y+dy[i]
            if curr_x>=0 and curr_x<m and curr_y>=0 and curr_y<n and ground[curr_x][curr_y]==1 and visitied[curr_x][curr_y]==0:

                bachu.remove([curr_x,curr_y])
                dfs(curr_x,curr_y)


for tc in range(t):
    c=0
    m,n,k=map(int,input().split())
    ground=[[0]*n for i in range(m)]
    visitied=[[0]*n for i in range(m)]
    bachu=[]
    for i in range(k):
        x,y=map(int,input().split())
        ground[x][y]=1
        bachu.append([x,y])

    while bachu!=[]:
        a=bachu.pop(0)
        dfs(a[0],a[1])
        c+=1
    print(c)
        

        
    

    

