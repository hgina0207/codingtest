n=int(input())
t=[]
for i in range(n):
    s,e=map(int,input().split())
    t.append([s,e])

t.sort(key=lambda x:x[0])
t.sort(key=lambda x:x[1])

c=1
end=t[0][1]
for i in range(1,n):
    if t[i][0]>=end:
        c+=1
        end=t[i][1]
print(c)