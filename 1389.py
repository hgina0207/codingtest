
n,m=map(int,input().split())
friends=[[1e9]*(n) for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    friends[a-1][b-1]=1
    friends[b-1][a-1]=1

for i in range(n):
    friends[i][i]=0

for k in range(n):
    for a in range(n):
        for b in range(n):
            friends[a][b]=min(friends[a][b],friends[a][k]+friends[k][b])

kb=[0]*n
for i in range(n):
    kb[i]=sum(friends[i])

print(kb.index(min(kb))+1)