import sys
import itertools


input=sys.stdin.readline

n=int(input())
power=[]

for i in range(n):
    power.append(list(map(int,input().split())))

min_diff=1e9
for start in itertools.combinations(range(n),n//2):
    s,l=0,0
    link=list(set(range(n))-set(start))
    for start_team in itertools.combinations(start,2):
        s+=power[start_team[0]][start_team[1]]
        s+=power[start_team[1]][start_team[0]]
    for link_team in itertools.combinations(link,2):
        l+=power[link_team[0]][link_team[1]]
        l+=power[link_team[1]][link_team[0]]
    min_diff=min(min_diff,abs(l-s))

print(min_diff)