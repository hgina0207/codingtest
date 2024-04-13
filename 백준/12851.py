from collections import deque
n,k=map(int,input().split())

q=deque()
q.append((n,0))
method=0
min_time=int(1e9)
dist=[int(1e9)]*100001
dist[n]=0
while q:
    now,time=q.popleft()
    
    if min_time<time:
        continue
    if now==k:
        if min_time>time:
            min_time=time
            method=1
        elif min_time==time:
            method+=1
        else:
            continue
    if 0<=now*2<=100000 and dist[now*2]>=time+1:
        dist[now*2]=time+1
        q.append((now*2,time+1))

    if 0<=now-1<=100000 and dist[now-1]>=time+1:
        dist[now-1]=time+1
        q.appendleft((now-1,time+1))
    
    if 0<=now+1<=100000 and dist[now+1]>=time+1:
        dist[now+1]=time+1
        q.append((now+1,time+1))
        
print(min_time)
print(method)