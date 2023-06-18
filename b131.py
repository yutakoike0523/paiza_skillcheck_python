s= list(map(int,input().split()))
N,M=s[0],s[1]
ways=[]
money=0
for i in range(0,N):
    t= list(map(int,input().split()))
    ways.append(t)
x=int(input())
X=0
Y=0
for i in range(0,x):
    t=list(map(int,input().split()))
    p,q=t[0]-1,t[1]-1
    if Y==q: 
        X=p
        Y=q
    elif Y<q:
        money+=ways[p][q]-ways[p][Y]
        X=p
        Y=q
    elif Y>q:
        money+=ways[p][Y]-ways[p][q]
        X=p
        Y=q
print(money) 
