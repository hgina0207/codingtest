import sys
sys.setrecursionlimit(10**6)
n=int(input())

def dp(x,y):
    if(y<0): return
    if x==0:
        cost[y][x]=cost[y][x]+min(cost[y+1][1],cost[y+1][2])
        dp(1,y)
    elif x==1:
        cost[y][x]=cost[y][x]+min(cost[y+1][0],cost[y+1][2])
        dp(2,y)
    else:
        cost[y][x]=cost[y][x]+min(cost[y+1][0],cost[y+1][1])
        dp(0,y-1)
cost=[]
for i in range(n):
    r,g,b=map(int,input().split())
    cost.append([r,g,b])
dp(0,n-2)
print(min(cost[0]))