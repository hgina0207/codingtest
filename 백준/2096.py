import copy
n=int(input())

num=(list(map(int,input().split())))
min_dp=num
max_dp=num

for i in range(n-1):
    num=(list(map(int,input().split())))

    min_dp=[min(min_dp[0],min_dp[1])+num[0],min(min_dp)+num[1],min(min_dp[1],min_dp[2])+num[2]]
    max_dp=[max(max_dp[0],max_dp[1])+num[0],max(max_dp)+num[1],max(max_dp[1],max_dp[2])+num[2]]



print(max(max_dp),min(min_dp))            