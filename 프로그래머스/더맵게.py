import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville);
    if scoville[0]>=K:
        return 0;
    
    def check():
        for s in scoville:
            if s<K:
                return False
        return True
    while len(scoville)>=2 and not check():
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b)
        answer+=1
    if check():
        return answer
    else: return -1