import math
def solution(m, n, startX, startY, balls):
    answer = []
    
    for endX,endY in balls:
        min_dist=1e9
        
        #위쪽변
        if not (startX==endX and startY<endY):
            min_dist=min(min_dist,(startX-endX)**2+(2*n-endY-startY)**2)
        #아래변
        if not (startX==endX and startY>endY):
            min_dist=min(min_dist,(startX-endX)**2+((startY+endY)**2))
        #왼쪽변
        if not (startY==endY and startX>endX):
            min_dist=min(min_dist,(startY-endY)**2+((startX+endX)**2))
        ##오른변
        if not (startY==endY and startX<endX):
            min_dist=min(min_dist,(startY-endY)**2+((2*m-endX-startX)**2))
            
        answer.append(min_dist)
            
            
    return answer