from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())

q=deque()
q.append((n,1))

flag=False
cnt=1
while q:
    num,cnt=q.popleft()
    if num==m:
        flag=True
        break
    if num*2<=m:
        q.append((num*2,cnt+1))
    if num*10+1<=m:
        q.append((num*10+1,cnt+1))
if flag:
    print(cnt)
else:
    print(-1)