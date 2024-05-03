def solution(number, k):
    answer=[]
    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k>0:
            while answer[-1]<num:
                answer.pop()
                k-=1
                if k==0 or not answer:
                    break
        answer.append(num)
    answer=answer[:-k] if k>0 else answer
    return "".join(answer)