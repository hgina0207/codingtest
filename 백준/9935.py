import sys
input=sys.stdin.readline
string=list(input().strip())
bumb=list(input().strip())
stack=[]

for i in range(len(string)):
    stack.append(string[i])
    if string[i]==bumb[-1]:
        flag=True
        stack_idx=len(stack)-1
        for j in range(len(bumb)-1,-1,-1):
            if stack[stack_idx-(len(bumb)-j-1)]!=bumb[j]:
                flag=False
                break
        if flag:
            for i in range(len(bumb)):
                stack.pop()
if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))