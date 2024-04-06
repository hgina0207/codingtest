import sys
input=sys.stdin.readline
t=int(input())

for _ in range(t):
    oper=input().strip()
    n=int(input())
    arr=input().strip('[]\n')
    if arr!='':    
        arr=list(map(int,arr.split(',')))
    start,end=0,n-1
    if n==0: end=0
    is_reversed=-1
    is_error=-1
    for o in oper:
        if o=='R':
            is_reversed*=-1
            tmp=start
            start=end
            end=tmp
        elif o=='D':
            n-=1
            if n<0:
                is_error=1
                break
            if n==0:
                continue
            if is_reversed>0:
                start-=1
                if start<end: 
                    is_error=1
                    break
            else:
                start+=1
                if start>end: 
                    is_error=1
                    break

        if n<0 or start<0 or end<0:
            is_error=1
            break

        
    if is_error==1:
        print('error')
    else:
        if n==0:
            print('[]')
        else:
            print('[',end='')
            if is_reversed<0:
                for i in range(start,end):
                    print(arr[i],end=',')
            else:
                for i in range(start,end,-1):
                    print(arr[i],end=',')
            print(arr[end],end='')
            print(']')