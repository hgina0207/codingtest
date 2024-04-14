def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    ai,bi=0,0
    while ai<len(A):
        if A[ai]<B[bi]:
            answer+=1
            bi+=1
        ai+=1
    return answer