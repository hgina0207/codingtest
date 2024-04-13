import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
visited=[-1]*100001
q=deque()
q.append(n)
visited[n]=0
while q:
    loc=q.popleft()
    if loc==k:
        print(visited[loc])
        break
    else:
        if 0<=loc*2<=100000 and visited[loc*2]==-1:
            q.appendleft(loc*2)
            visited[loc*2]=visited[loc]
        if 0<=loc-1<=100000 and visited[loc-1]==-1:
            q.append(loc-1)
            visited[loc-1]=visited[loc]+1
        if 0<=loc+1<=100000 and visited[loc+1]==-1:
            q.append(loc+1)
            visited[loc+1]=visited[loc]+1
        