from collections import deque
def solution(n, edge):
    answer = 0
    max_depth=1
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    q=deque()
    q.append((1,0))
    visited[1]=True
    while q:
        node,depth=q.popleft()
        has_next_node=False
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append((next_node,depth+1))
                visited[next_node]=True
                has_next_node=True
        if not has_next_node:
            if depth>max_depth:
                max_depth=depth
                answer=1
            elif depth==max_depth:
                answer+=1
                
    return answer