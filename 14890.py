import sys
import copy
input=sys.stdin.readline

n,L=map(int,input().split())
road_init=[]

for _ in range(n):
    road_init.append(list(map(int,input().split())))

res=0


road=copy.deepcopy(road_init)
for i in range(n):
    same_block1=1
    plag1=0
    j=1
    while j<n:
        if road[i][j-1]==road[i][j]:
            same_block1+=1
        elif road[i][j-1]-road[i][j]==1 and j+L<=n:
            for l in range(1,L):
                if road[i][j+l]!=road[i][j]:
                    plag1=1
                    break
            if plag1==1:break
            same_block1=0
            j+=L-1
        elif road[i][j-1]-road[i][j]==-1:
            if same_block1<L: 
                plag1=1
                break
            else: 
                same_block1=1
        else:
            plag1=1
            break
        j+=1
    if plag1==0: res+=1
road=copy.deepcopy(road_init)   
for i in range(n):
    same_block2=1
    plag2=0
    j=1
    while j<n:
        if road[j-1][i]==road[j][i]:
            same_block2+=1
        elif road[j-1][i]-road[j][i]==1 and j+L<=n:
            for l in range(1,L):
                if road[j+l][i]!=road[j][i]:
                    plag2=1
                    break
            if plag2==1:break
            same_block2=0
            j+=L-1
        elif road[j-1][i]-road[j][i]==-1:
            if same_block2<L: 
                plag2=1
                break
            else: 
                same_block2=1
        else:
            plag2=1
            break
        j+=1
    if plag2==0: res+=1
print(res)