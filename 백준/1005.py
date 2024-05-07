import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
t=int(input())

def dfs(now,rules,cities,dp):
    if len(rules[now])==0:
        return cities[now]
    if dp[now]!=-1:
        return dp[now]
    max_time=0
    for i in range(len(rules[now])):
        max_time=max(max_time,dfs(rules[now][i],rules,cities,dp))
    dp[now]=max_time+cities[now]
    return dp[now]

for _ in range(t):
    n,k=map(int,input().split())
    cities=[0]+list(map(int,input().split()))
    rules=[[] for _ in range(n+1)]
    dp=[-1]*(n+1)
    for _ in range(k):
        a,b=map(int,input().split())
        rules[b].append(a)
    w=int(input())
    print(dfs(w,rules,cities,dp))

