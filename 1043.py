import copy
n,m=map(int,input().split())
true_input=list(map(int,input().split()))

party=[]
people=[[] for i in range(n+1)]
for i in range(m):
    party.append(list(map(int,input().split())))
    party[i].pop(0)
    for j in party[i]:
        people[j].append(i)
def find_true(true_people):
    for p in people[true_people]:
        if party[p]!=[]:
            party_num=copy.deepcopy(party[p])
            party[p]=[]
            for i in party_num:
                if i!=true_people:
                    find_true(i)

if true_input[0]==0:
    print(m)
else:
    true_input.pop(0)
    for i in true_input:
        find_true(i)
    
    false_count=0
    for i in party:
        if i!=[]:
            false_count+=1
    print(false_count)

