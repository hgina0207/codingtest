import sys
import copy
input=sys.stdin.readline
topni=[]
for i in range(4):
    topni.append(list(input().rstrip()))

n=int(input())
top=[0]*4
score=0
for i in range(n):
    k,d=map(int,input().rstrip().split())
    top_sample=copy.deepcopy(top)
    d_sample=d
    for j in range(k-1,3):
        topni_i_3=(top[j]+2)%8
        topni_j_7=(top[j+1]+6)%8
        if topni[j][topni_i_3]!=topni[j+1][topni_j_7]:
            top_sample[j+1]=(top[j+1]+d_sample)%8
            d_sample*=-1
        else: break

    d_sample=d
    for j in range(k-1,0,-1):
        topni_i_7=(top[j]+6)%8
        topni_j_3=(top[j-1]+2)%8
        if topni[j][topni_i_7]!=topni[j-1][topni_j_3]:
            top_sample[j-1]=(top[j-1]+d_sample)%8
            d_sample*=-1
        else: break

    top_sample[k-1]=(top[k-1]-d)%8
    for j in range(4):
        top[j]=top_sample[j]
for j in range(4):
    if topni[j][top[j]]=='1':
        score+=2**j
print(score)
    
