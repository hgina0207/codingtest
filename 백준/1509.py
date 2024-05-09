import sys
input=sys.stdin.readline

string=input().strip()
n=len(string)
p=[[0]*n for _ in range(n)]

for i in range(n):
    p[i][i]=1

for i in range(1,n):
    if string[i]==string[i-1]:
        p[i-1][i]=1

for i in range(3,n+1):
    for j in range(n-i+1):
        k=j+i-1
        if string[j]==string[k] and p[j+1][k-1]:
            p[j][k]=1

dp=[1e9]*(n+1)
dp[n]=0
for e in range(n):
    for s in range(e+1):
        if p[s][e]:
            dp[e]=min(dp[e],dp[s-1]+1)

print(dp[n-1])