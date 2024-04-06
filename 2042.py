import sys
input=sys.stdin.readline

def init_tree(start,end,node):
    if start==end:
        tree[node]=arr[start]
        return tree[node]
    mid=(start+end)//2
    tree[node]=init_tree(start,mid,node*2)+init_tree(mid+1, end, node*2+1)

def update_tree(start,end,node,idx,diff):
    if idx<start or idx>end:
        return
    tree[node]+=diff
    mid=(start+end)//2
    update_tree(start, mid, node*2, idx, diff)
    update_tree(mid+1, end, node*2+1, idx, diff)

def get_sum(start,end,node,left,right):
    if left<start or right>end:
        return
    if left<=end and right>=start:
        return tree[node]
    mid=(start+end)//2
    get_sum(start, mid, node*2, left, right)
    get_sum(mid+1, end, node*2+1, left, right)
N,M,K=map(int,input().split())
arr=[]
tree=[]
for i in range(1,N+1):
    arr[i].append(int(input))

init_tree(1,N,1)
for i in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        update_tree(1,N,1,b,c-arr[start])
        arr[b]=c
    elif a==2:
        print(get_sum(1,N,1,left,right))