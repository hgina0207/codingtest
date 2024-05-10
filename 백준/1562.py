from itertools import permutations
n=int(input())
if n<10:
    print(0)
else:
    answer=0
    def is_stair(num):
        print(num)
        for i in range(1,n):
            if abs(num[i-1]-num[i])>1:
                return False
        return True
    for p in permutations(range(10),n):
        print(p)
        if p[0]==0:
            continue
        if is_stair(''.join(p)):
            answer+=1
    print(answer)