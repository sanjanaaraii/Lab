n=int(input("enter n"))
r=int(input("enter r"))
nr=n-r
fact1=1
fact2=1
fact3=1
while(n!=0):
    fact1=fact1*(n)
    n-=1
while(r!=0):
    fact2=fact1*(r)
    r-=1
while(nr!=0):
    fact3=fact1*(nr)
    nr-=1
ans=(fact1)//(fact2*fact3)
print(ans)