n=int(input())
rev=0
t=n
while t>0:
    r=t%10
    rev=(rev*10)+r
    t=t//10
if n== rev:
    print("yes")
else:
    print("no")
