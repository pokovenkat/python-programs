n=int(input())
k=int(input())
arr=[]
tot=0
for i in range(n):
    arr.append(int(input()))
for i in range (k):
    tot+=arr[i]
print(tot)
