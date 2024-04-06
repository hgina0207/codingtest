N,B=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]
def multiple(a,b):
    res=[[] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            num=0
            for j in range(N):
                num+=a[k][j]*b[j][i]
            res[k].append(num%1000)
    return res
def power(b,matrix):
    if b==1:
        return matrix
    else:
        res=power(b//2,matrix)
        if b%2==0:
            res=multiple(res,res)
        else:
            res=multiple(multiple(res,res),matrix)

        return res

res=power(B,arr)
for i in range(N):
    for j in range(N):
        print(res[i][j]%1000,end=' ')
    print()