tc=int(input())

def bf():
    time=[1e9 for _ in range(n+1)]
    time[1]=0
    for i in range(n):
        for r in road:
            s,e,t=r
            if time[e]>time[s]+t:
                time[e]=time[s]+t
                if i==n-1:
                    return 'YES'
    return 'NO'
for _ in range(tc):
    n,m,w=map(int,input().split())
    road=[]
    for i in range(m):
        s,e,t=map(int,input().split())
        road.append([s,e,t])
        road.append([e,s,t])
    for _ in range(w):
        s,e,t=map(int,input().split())
        road.append([s,e,-t])
    print(bf())