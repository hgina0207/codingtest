
import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
dp=[1]*n

for i in range(0,n):
    for j in range(i):
        if num[i]>num[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))