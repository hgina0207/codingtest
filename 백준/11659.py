n,m=map(int,input().split())
num=[0]+list(map(int,input().split()))
max_i=0
min_i=0
idx=[]
for t in range(m):
    i,j=map(int,input().split())
    max_i=max([max_i,i,j])
    min_i=min([min_i,i,j])
    idx.append([i,j])
for i in range(min_i,max_i):
    num[i+1]=num[i]+num[i+1]
for i in range(m):
    print(num[idx[i][1]]-num[idx[i][0]-1])