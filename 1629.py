a,b,c=map(int,input().split())

def calcul(d,e,f):
    if e==1:
        return d%f
    else:
        if e%2==0:
            return calcul(d,e//2,f)**2%f
        else:
            return calcul(d,e//2,f)**2*d%f

print(calcul(a,b,c))