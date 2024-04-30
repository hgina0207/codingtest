def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start=h1*3600+m1*60+s1
    end=h2*3600+m2*60+s2
    
    if start==0*3600 or start==12*3600:
        answer+=1
    
    while start<end:
        #1시간에 360/12=30도 -> 1초에 30/3600=1/120
        #1분에 360/60=6도 -> 1초에 6/60=1/10
        #1초에 360/60=6도
        hCurAngle=start/120%360
        mCurAngle=start/10%360
        sCurAngle=start*6%360
        
        hNextAngle=360 if (start+1)/120%360==0 else (start+1)/120%360
        mNextAngle=360 if (start+1)/10%360==0 else (start+1)/10%360
        sNextAngle=360 if (start+1)*6%360==0 else (start+1)*6%360
        
        if hCurAngle>sCurAngle and hNextAngle<=sNextAngle:
            answer+=1
        if mCurAngle>sCurAngle and mNextAngle<=sNextAngle:
            answer+=1
        if hNextAngle==sNextAngle and hNextAngle==mNextAngle:
            answer-=1
            
        start+=1
    return answer