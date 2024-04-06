from collections import deque
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
res_set=set()
q=deque()
visited=[False]*n
def dfs(start):
    if len(q)==m:
        res_set.add(tuple(q))
        return
    else:
        for i in range(0,n):
            if len(q)==0 or not visited[i]:
                q.append(arr[i])
                visited[i]=True
                dfs(i+1)
                q.pop()
                visited[i]=False
dfs(0)
res=list(res_set)
res.sort()
for r in res:
    print(" ".join(map(str,r)))