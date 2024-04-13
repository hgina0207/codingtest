t=int(input())
for i in range(t):
    N=int(input())
    arr_0=[1,0]
    arr_1=[0,1]
    if N>1:
        for i in range(2,N+1):
            arr_0.append(arr_0[i-1]+arr_0[i-2])
            arr_1.append(arr_1[i-1]+arr_1[i-2])
    print(arr_0[N], arr_1[N])