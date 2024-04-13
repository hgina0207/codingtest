from collections import deque
n,m=map(int,input().split())
q=deque()
def dfs(cnt,now):
    if cnt==m:
        for i in range(m):
            print(q[i],end=' ')
        print()
        q.pop()
        return
    else:
        for i in range(now,n+1):
            q.append(i)
            dfs(cnt+1,i)
            if i==n and len(q)!=0:
                q.pop()
dfs(0,1)