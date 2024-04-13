import sys
input=sys.stdin.readline
matrix=[[1,1],[1,0]]
n=int(input())
C=1000000007
def multiple(mat1,mat2):
    a=mat1[0][0]*mat2[0][0]+mat1[0][1]*mat2[1][0]
    b=mat1[0][0]*mat2[0][1]+mat1[0][1]*mat2[1][1]
    c=mat1[1][0]*mat2[0][0]+mat1[1][1]*mat2[1][0]
    d=mat1[1][0]*mat2[0][1]+mat1[1][1]*mat2[1][1]
    return [[a%C,b%C],[c%C,d%C]]
def power(d):
    if d==1:
        return matrix
    else:
        tmp=power(d//2)
        if d%2==0:
            return multiple(tmp,tmp)
        else:
            return multiple(multiple(tmp,tmp),matrix)

res=power(n)
print(res[0][1])