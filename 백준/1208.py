import sys
from collections import defaultdict
from itertools import combinations
input=sys.stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
answer=0

def make_combi(nums,dic):
    for i in range(1,len(nums)+1):
        for c in combinations(nums,i):
            dic[sum(c)]+=1

dic1=defaultdict(int)
dic2=defaultdict(int)
make_combi(arr[:n//2],dic1)
make_combi(arr[n//2:],dic2)

answer+=dic1[s]+dic2[s]

for s1 in dic1:
    if s-s1 in dic2:
        answer+=dic1[s1]*dic2[s-s1]

print(answer)