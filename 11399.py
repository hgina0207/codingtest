n=int(input())
time=list(map(int,input().split()))
time.sort()
dp=[0]*len(time)
dp[0]=time[0]
for i in range(1,len(time)):
    dp[i]=dp[i-1]+time[i]
print(sum(dp))