from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    shuttleTime=9*60-t
    shuttle=deque()
    timeIdx=0
    print(shuttleTime)
    while n>0:
        n-=1
        shuttleTime+=t
        people=0
        while timeIdx<len(timetable):
            hour,minute=map(int,timetable[timeIdx].split(":"))
            time=hour*60+minute
            if time<=shuttleTime:
                if n==0:
                    shuttle.append(time)
                timeIdx+=1
                people+=1
                if people==m:
                    break
            else:
                break
    print(shuttle,shuttleTime)           
    answerTime=shuttleTime
    if len(shuttle)>=m:
        answerTime=shuttle[m-1]-1
    
    hour=int(answerTime/60)
    minute=answerTime%60
    answer+="0"+str(hour)+":" if hour<10 else str(hour)+":"
    answer+="0"+str(minute) if minute<10 else str(minute)               
                
    return answer