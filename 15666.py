import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()

res=set()
q=deque()
def solve(cnt,idx):
    if cnt==m:
        if tuple(q) not in res:
            for i in range(m):
                print(q[i],end=' ')
            print()
            res.add(tuple(q))
        q.pop()
        return
    else:
        for i in range(idx,n):
            q.append(num[i])
            solve(cnt+1,i)
            if i==n-1 and len(q)!=0:
                q.pop()

solve(0,0)