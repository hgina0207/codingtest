c,n=map(int,input().split())
dp=[int(1e6) for i in range(c+101)]
dp[0]=0
city=[]
for i in range(n):
    a,b=map(int,input().split())
    city.append([a,b])

city.sort()
for a,b in city:
    for i in range(b,c+101):    
        dp[i]=min(dp[i-b]+a,dp[i])
print(min(dp[c:c+101]))