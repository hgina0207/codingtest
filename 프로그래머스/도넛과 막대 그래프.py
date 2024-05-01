def solution(edges):
    answer = [0,0,0,0]
    nodeCnt={}
    
    for e in edges:
        a=e[0]
        b=e[1]
        if not nodeCnt.get(a):
            nodeCnt[a]=[0,0]
        if not nodeCnt.get(b):
            nodeCnt[b]=[0,0]
        nodeCnt[a][0]+=1
        nodeCnt[b][1]+=1
        
    for k,v in nodeCnt.items():
        if v[0]>=2 and v[1]==0:
            answer[0]=k
        elif v[0]>=2 and v[1]>=2:
            answer[3]+=1
        elif v[0]==0 and v[1]>=1:
            answer[2]+=1
    answer[1]=nodeCnt[answer[0]][0]-answer[2]-answer[3]
            
    return answer