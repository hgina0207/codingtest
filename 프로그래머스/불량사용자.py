from itertools import permutations
import re
def solution(user_id, banned_id):
    answer = 0
    n=len(banned_id)
    res=set()
    for i in range(n):
        banned_id[i]=banned_id[i].replace('*','.')
    for p in permutations(user_id,n):
        flag=True
        for i in range(n):
            if len(banned_id[i])==len(p[i]) and re.match(banned_id[i],p[i]):
                continue
            else: 
                flag=False
                break
        if flag:
            print(sorted(p))
            res.add(tuple(sorted(p)))
    answer=len(res)
    return answer