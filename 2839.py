n=int(input())
res=-1
q=n//5
r=n%5
while q>=0:
    if r==0:
        res=q
        break
    elif r%3==0:
        res=q+r//3
        break
    q-=1
    r=n-q*5

print(res)