import sys
from collections import deque
input=sys.stdin.readline



n,m=map(int,input().split())
visited=[False]*(n+1)
def dfs(num,cnt):
    if cnt==m:
        for i in range(1,n+1):
            if visited[i]: print(i,end=' ')
        print()
        return
    else:
        for i in range(num+1,n+1):
            if n-i>=m-(cnt+1):
                visited[i]=True
                dfs(i,cnt+1)
                visited[i]=False
            else: break
if n==m: 
    visited[1]=True
    dfs(1,1)
else:
    for i in range(1,n-m+2):
        visited[i]=True
        dfs(i,1)
        visited[i]=False