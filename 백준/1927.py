import heapq,sys
input=sys.stdin.readline
heap=[]
n=int(input())
for _ in range(n):
    num=int(input())
    if num==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)