def solution(a):
    balloon=[False]*len(a)
    left,right=1e9,1e9
    for i in range(len(a)):
        if a[i]<left:
            left=a[i]
            balloon[i]=True
        if a[-1-i]<right:
            right=a[-1-i]
            balloon[-1-i]=True
            
    return sum(balloon)