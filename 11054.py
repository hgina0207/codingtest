import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
num_rev=list(reversed(num))
dp_increase=[1]*n
dp_decrease=[1]*n
for i in range(n):
    for j in range(i):
        if num[i]>num[j]:
            dp_increase[i]=max(dp_increase[j]+1,dp_increase[i])
        if num_rev[i]>num_rev[j]:
            dp_decrease[i]=max(dp_decrease[j]+1,dp_decrease[i])

max_num=0
for i in range(n):
    if dp_decrease[n-i-1]+dp_increase[i]>max_num:
        max_num=dp_decrease[n-i-1]+dp_increase[i]

print(max_num-1)