import sys
sys.setrecursionlimit(10**9)

n=int(input())
tree={}


def preorder(alpha):
    if alpha!='.':
        print(alpha,end='')
        preorder(tree[alpha][0])
        preorder(tree[alpha][1])

def inorder(alpha):
    if alpha!='.':
        inorder(tree[alpha][0])
        print(alpha,end='')
        inorder(tree[alpha][1])

def postorder(alpha):
    if alpha!='.':
        postorder(tree[alpha][0])
        postorder(tree[alpha][1])
        print(alpha,end='')

for _ in range(n):
    a,b,c=input().split()
    tree[a]=[b,c]

preorder('A')
print()
inorder('A')
print()
postorder('A')