import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
pre=[]

while True:
    try:
        pre.append(int(input().rstrip()))
    except:
        break

def post(start,end):
    if start>end:
        return
    mid=end+1

    for i in range(start+1,end+1):
        if pre[start]<pre[i]:
            mid=i
            break
    post(start+1,mid-1)
    post(mid,end)
    print(pre[start])

post(0,len(pre)-1)