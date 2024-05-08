import sys
import heapq
input=sys.stdin.readline

n,k=map(int,input().split())
bosuk=[]
bag=[]

for _ in range(n):
    m,v=map(int,input().split())
    heapq.heappush(bosuk,(m,v))

for _ in range(k):
    bag.append(int(input()))
bag.sort()

answer=0
tmp=[]
for b in bag:
    while bosuk and b>=bosuk[0][0]:
        heapq.heappush(tmp,-heapq.heappop(bosuk)[1])
    if tmp:
        answer-=heapq.heappop(tmp)
print(answer)