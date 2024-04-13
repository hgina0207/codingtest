n,r,c=map(int,input().split())
total=(2**n)
res=0
while total>1:
    if r<total/2 and c<total/2:
        res+=((total/2)**2)*0
    elif r<total/2 and c>=total/2:
        res+=((total/2)**2)*1
        c-=total/2
    elif r>=total/2 and c<total/2:
        res+=((total/2)**2)*2
        r-=total/2
    elif r>=total/2 and c>=total/2:
        res+=((total/2)**2)*3
        r-=total/2
        c-=total/2
    

    total/=2
    
    
print(int(res))