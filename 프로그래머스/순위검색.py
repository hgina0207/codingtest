from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    info_dict={}
    for infomation in info:
        i=infomation.split()
        condition=i[:-1]
        score=int(i[-1])
        for j in range(5):
            for c in combinations(condition,j):
                key=''.join(c)
                if key in info_dict:
                    info_dict[key].append(score)
                else:
                    info_dict[key]=[score]
    for k in info_dict:
        info_dict[k].sort()
        
    for q in query:
        q=q.replace("and"," ")
        q=q.replace("-"," ")
        tmp=list(q.split())
        condition=tmp[:-1]
        score=int(tmp[-1])
        key=''.join(condition)
        
        if key in info_dict:
            scores=info_dict[key]
            loc=bisect_left(scores,score)
            answer.append(len(scores)-loc)
        else:
            answer.append(0)
            
        
        
    return answer