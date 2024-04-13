import sys
n,m=map(int,sys.stdin.readline().split())
poketmon1={}
poketmon2={}
for i in range(n):
    name=sys.stdin.readline().rstrip()
    poketmon1[str(i+1)]=name
    poketmon2[name]=i+1
for i in range(m):
    question=sys.stdin.readline().rstrip()
    if question[0].isdigit():
        print(poketmon1[question])
    else: print(poketmon2[question])