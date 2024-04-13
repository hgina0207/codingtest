arr=input()
stack=[]
md=['*','/']
pm=['+','-']
ans=""
for s in arr:
    if s>='A' and s<='Z':
        ans+=s
    elif s==')':
        while stack:
            c=stack.pop()
            if c=='(':
                break
            else: ans+=c
    elif not stack or (stack[-1] in pm and s in md) or s=='(' or stack[-1]=='(':
        stack.append(s)
    
    elif stack[-1] in md and s in md:
        ans+=stack.pop()
        stack.append(s)
    elif stack[-1] in md and s in pm:
        while stack:
            c=stack[-1]
            if c in md:
                ans+=stack.pop()
            elif c in pm:
                ans+=stack.pop()
                break
            elif c=='(':
                break
        stack.append(s)
    elif stack[-1] in pm and s in pm:
        ans+=stack.pop()
        stack.append(s)
while stack:
    ans+=stack.pop()
print(ans)