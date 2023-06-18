s= list(map(int,input().split()))
N,M=s[0],s[1]
t= list(map(int,input().split()))
A,B,C=t[0],t[1],t[2]
sum=0
for i in range(0,N):
    X=int(input())
    gain=C*X-A-B*M
    if gain<0:
        sum+=1
print(sum)